#!/usr/bin/env python3
"""check_note.py: is a note short, typed and linked? The eval for note_writer.

python skills/notes/note_writer/scripts/check_note.py <vault_or_note.md> [--budget 120] [--stubs]
Exit 1 when any note fails. A pass prints OK.

Fails (error):
  - frontmatter missing a field: title, date_created, description, type, domain, reference
  - type not one of the eight, or the folder does not match the type
  - title not lowercase, or title differs from the file name
  - body over the word budget (default 120; link-only lines do not count, so a hub of links is fine)
Warns:
  - a bullet over 20 words
  - no wikilink in the note (an orphan idea)
  - no `# References` heading at the end
--stubs lists unresolved [[links]]: the inventory of unknowns.
Collisions (error): two files with one name. Obsidian resolves [[name]] to one file only, so a link would go to the wrong page.
  Checked inside the notes tree, and against a sibling `wiki/` folder (the merged vault: <vault>/notes and <vault>/wiki), or --also <dir>.
Stdlib only. Reads YAML frontmatter with a small parser (flat keys and lists, as the vault writes them).
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

TYPES = {"technology": "1_technology", "technique": "2_technique", "research": "3_research", "tool": "4_tool",
         "concept": "5_concept", "prompt": "6_prompt", "bookmark": "7_bookmark", "other": "99_other"}
REQUIRED = ["title", "date_created", "description", "type", "domain", "reference"]
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
LINK_ONLY = re.compile(r"^\s*(?:[-*]\s*)?(?:\[\[[^\]]+\]\][\s,;:.\-]*)+$")


def split(text: str) -> tuple[dict[str, object], str]:
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    if not m: return {}, text
    fm: dict[str, object] = {}; key = None
    for line in m.group(1).splitlines():
        if re.match(r"^\s+-\s", line) and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list): fm[key].append(line.split("-", 1)[1].strip().strip('"'))  # type: ignore
        elif ":" in line and not line.startswith(" "):
            key, _, v = line.partition(":"); key = key.strip(); v = v.strip()
            fm[key] = [] if v in ("", "[]") and key in ("domain", "reference") else v.strip('"')
    return fm, m.group(2)


def words(body: str) -> int:
    n = 0
    for line in body.splitlines():
        if line.strip().startswith("#") or LINK_ONLY.match(line) or not line.strip(): continue
        n += len(re.sub(r"https?://\S+", "", re.sub(r"\[\[([^\]]+)\]\]", r"\1", line)).replace("-", " ").split())
    return n


def check(path: Path, root: Path | None, budget: int) -> tuple[list[str], list[str]]:
    errs, warns = [], []
    fm, body = split(path.read_text(encoding="utf-8"))
    for k in REQUIRED:
        if k not in fm: errs.append(f"missing frontmatter: {k}")
    t = fm.get("type")
    if t not in TYPES: errs.append(f"type '{t}' not one of {sorted(TYPES)}")
    elif root is not None and path.parent.name != TYPES[str(t)]:
        errs.append(f"folder {path.parent.name} does not match type {t} ({TYPES[str(t)]})")
    title = str(fm.get("title", ""))
    if title and title != title.lower(): errs.append("title is not lowercase")
    if title and title != path.stem: errs.append(f"title '{title}' differs from file name '{path.stem}'")
    n = words(body)
    if n > budget: errs.append(f"body is {n} words, budget {budget}")
    for line in body.splitlines():
        if re.match(r"^\s*[-*]\s", line) and not LINK_ONLY.match(line) and len(line.split()) > 21:
            warns.append("bullet over 20 words: " + line.strip()[:50] + "...")
    if not LINK.search(body) and not fm.get("reference"): warns.append("no wikilink and no reference")
    if "# References" not in body: warns.append("no '# References' heading")
    return errs, warns


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target"); ap.add_argument("--budget", type=int, default=120); ap.add_argument("--stubs", action="store_true"); ap.add_argument("--also", action="append", default=[], help="another tree whose file names must not collide")
    a = ap.parse_args()
    t = Path(a.target).expanduser()
    root = t if t.is_dir() else None
    files = sorted(p for p in (t.rglob("*.md") if root else [t]) if not (root and "_obsidian" in p.relative_to(root).parts)
                   and p.name != "AGENTS.md" and not (root and p.relative_to(root).parts[0].startswith(".")))
    bad = 0; names = {p.stem.lower() for p in files}; stubs: dict[str, set[str]] = {}
    for p in files:
        errs, warns = check(p, root, a.budget)
        for e in errs: print(f"ERROR {p.name}: {e}")
        for w in warns: print(f"warn  {p.name}: {w}")
        bad += bool(errs)
        for l in LINK.findall(p.read_text(encoding="utf-8")):
            if l.strip().lower() not in names: stubs.setdefault(l.strip(), set()).add(p.stem)
    if root is not None:
        others = [Path(x) for x in a.also] + ([root.parent / "wiki"] if (root.parent / "wiki").is_dir() else [])
        seen: dict[str, Path] = {}
        for p in files:
            k = p.stem.lower()
            if k in seen:
                print(f"ERROR collision: '{p.stem}' is in {seen[k].parent.name} and {p.parent.name}"); bad += 1
            seen[k] = p
        for o in others:
            for q in o.rglob("*.md"):
                if q.stem.lower() in seen and "raw" not in q.parts:
                    print(f"ERROR collision: '{q.stem}' is a note and also {q}"); bad += 1
    if a.stubs:
        print("stubs (unknown terms, fill when learned):")
        for s, by in sorted(stubs.items()): print(f"  [[{s}]] <- {', '.join(sorted(by))}")
    print(f"{len(files)} notes, {bad} failing")
    if bad: return 1
    print("OK"); return 0


if __name__ == "__main__":
    sys.exit(main())
