#!/usr/bin/env python3
"""link_skills.py: link the phase 2 skills the notes system borrows into skills/notes/linked/.

python skills/notes/link_skills.py          create the links (idempotent)
python skills/notes/link_skills.py --check  verify, exit 1 if a link is missing or wrong

One source of truth: the skill stays in skills/phase_2/skills/<name>/. The link only makes it
findable from the notes folder. Links are local: git-ignored, never exported, and skipped by repo_map.py.

Windows: a symlink needs admin or Developer Mode. This script falls back to a directory junction,
which needs neither. POSIX: a symlink. Stdlib only. Never deletes real folders.
"""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINKS = HERE / "linked"
ROOT = next(p for p in HERE.parents if (p / ".rules").is_dir())
SRC = ROOT / "skills" / "phase_2" / "skills"
BORROWED = {
    "first_principles": "ambiguous bullet: what is law, convention, assumption. one why line",
    "second_order_thinking": "decision or default: the next event is the lesson. one next line",
    "socratic_questions": "opt-in, live: one question at a time",
    "writer_skill": "his writing style. short declaratives",
    "brevity_is_the_soul": "explanation stays, fluff goes",
    "diagrammer": "a concept that can be drawn is drawn: inline svg",
}


def is_link(p: Path) -> bool:
    if p.is_symlink():
        return True
    if os.name == "nt":  # junctions are not reported by is_symlink on older Pythons
        try:
            return bool(os.readlink(p))
        except OSError:
            return False
    return False


def points_to(p: Path, target: Path) -> bool:
    try:
        return p.resolve() == target.resolve()
    except OSError:
        return False


def make(link: Path, target: Path) -> str:
    try:
        os.symlink(target, link, target_is_directory=True)
        return "symlink"
    except (OSError, NotImplementedError):
        pass
    if os.name == "nt":
        r = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True, text=True)
        if r.returncode == 0:
            return "junction"
        raise SystemExit(f"cannot link {link.name}: {r.stdout.strip()} {r.stderr.strip()}")
    raise SystemExit(f"cannot symlink {link.name}")


def main() -> int:
    check = "--check" in sys.argv
    if not check: LINKS.mkdir(exist_ok=True)
    bad = 0
    for name in BORROWED:
        target, link = SRC / name, LINKS / name
        if not (target / "SKILL.md").is_file():
            print(f"MISSING source {target}"); bad += 1; continue
        if link.exists() or is_link(link):
            ok = points_to(link, target)
            print(("ok     " if ok else "WRONG  ") + name)
            bad += (not ok)
            continue
        if check:
            print("absent " + name); bad += 1; continue
        print(f"{make(link, target):10s}{name}")
    if bad:
        print(f"{bad} problem(s)"); return 1
    print("OK"); return 0


if __name__ == "__main__":
    sys.exit(main())
