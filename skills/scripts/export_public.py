#!/usr/bin/env python3
"""Export the public skeleton (phases, skills, rules, .agents, self-improve) to a separate folder. Allowlist copy, scrub, deny scan.
python skills/scripts/export_public.py <dest>          copy, scrub, regenerate REPO_MAP, scan
python skills/scripts/export_public.py <dest> --scan   scan only
Private by default: llm_wiki/, skill_factory/, Artifacts/, user-input-learning-text/ and every study topic stay here.
Files the public repo owns (README.md, LICENSE, docs/, .gitignore, .git) are never touched.
Exit 1 when the scan finds a private match. Do not push until it prints OK."""
from __future__ import annotations
import json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())

# only these leave the machine
ALLOW = [".agents", ".rules", ".github", ".grok", "skills", "Documentation",
         "AGENTS.md", "WORKFLOW_STUDY.md", "WORKFLOW_EXPERT_CAPTURE.md"]

# never copied, even inside an allowed folder
SKIP_PARTS = {"__pycache__", "examples", "built", "inbox", ".git", "node_modules", "video"}
SKIP_SUFFIX = (".pyc", ".mp4", ".mp3", ":Zone.Identifier", ".pdf")
PRIVATE_DIRS = ["llm_wiki", "skill_factory", "Artifacts", "user-input-learning-text"]


def skipped(rel: Path) -> bool:
    if any(p in SKIP_PARTS for p in rel.parts) or rel.name.endswith(SKIP_SUFFIX):
        return True
    # phase output folders: keep only their README
    return "output" in rel.parts[:3] and rel.parts[0] == "skills" and rel.name != "README.md"


# generic rules. his own terms (topic slugs, case ids, names) live in .export_private.json,
# which is not in ALLOW, so the list of what is private is itself never published.
SCRUB = [
    (r"[A-Za-z0-9._%+-]+@gmail\.com", "<your-email>"),
    (r"study-os", "study-os"),
]
DENY = [
    r"[A-Za-z0-9._%+-]+@(?!anthropic\.com|example\.com)[A-Za-z0-9-]+\.(?:com|in|org|net|io)\b",
    r"study-os", r"AKIA[0-9A-Z]{16}", r"\bsk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{20,}",
    r"xox[bp]-[A-Za-z0-9-]{10,}", r"BEGIN [A-Z ]*PRIVATE KEY",
]
PRIVATE_RULES = ROOT / ".export_private.json"
if PRIVATE_RULES.is_file():
    _cfg = json.loads(PRIVATE_RULES.read_text(encoding="utf-8"))
    SCRUB = [tuple(x) for x in _cfg.get("scrub", [])] + SCRUB
    DENY += _cfg.get("deny", [])


def is_text(p: Path) -> bool:
    try:
        p.read_text(encoding="utf-8")
        return True
    except (UnicodeDecodeError, OSError):
        return False


def export(dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for name in ALLOW:
        src, out = ROOT / name, dest / name
        if out.is_dir():
            shutil.rmtree(out)
        elif out.exists():
            out.unlink()
        files = [src] if src.is_file() else sorted(q for q in src.rglob("*") if q.is_file())
        for f in files:
            rel = f.relative_to(ROOT)
            if skipped(rel):
                continue
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if is_text(f):
                t = f.read_text(encoding="utf-8")
                for pat, rep in SCRUB:
                    t = re.sub(pat, rep, t, flags=re.S)
                target.write_text(t, encoding="utf-8", newline="")
            else:
                shutil.copy2(f, target)
    # the map is rebuilt inside dest, so it lists no private folder
    subprocess.run([sys.executable, str(dest / "skills/scripts/repo_map.py")], check=True, cwd=dest)


def scan(dest: Path) -> int:
    hits = []
    for d in PRIVATE_DIRS:
        if (dest / d).exists():
            hits.append(f"{d}/: private folder present")
    for f in sorted(q for q in dest.rglob("*") if q.is_file() and ".git" not in q.relative_to(dest).parts):
        if not is_text(f):
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for pat in DENY:
                if re.search(pat, line):
                    hits.append(f"{f.relative_to(dest).as_posix()}:{n}: {pat}")
    for h in hits:
        print("DENY", h)
    print("OK" if not hits else f"BLOCKED: {len(hits)} private match(es). do not push.")
    return 1 if hits else 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    dest = Path(sys.argv[1]).resolve()
    if dest == ROOT or ROOT in dest.parents:
        sys.exit("ERROR: dest must be outside the private Study-OS folder")
    if "--scan" not in sys.argv:
        export(dest)
    return scan(dest)


if __name__ == "__main__":
    raise SystemExit(main())
