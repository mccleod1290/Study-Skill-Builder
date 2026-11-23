#!/usr/bin/env python3
"""install_vault.py: scaffold the pentest note vault.

python skills/notes/vault_setup/scripts/install_vault.py <dest>            create or top up the vault
python skills/notes/vault_setup/scripts/install_vault.py <dest> --dry-run  list what would be written

Safe by design: never overwrites an existing file (notes, config, plugin), never deletes.
Re-run it after a kit update with --update-kit to refresh only the plugin, snippet, templates and bases.
Stdlib only. Obsidian itself is not started.
"""
from __future__ import annotations
import argparse, datetime, json, shutil, sys
from pathlib import Path

KIT = Path(__file__).resolve().parents[1] / "assets"
FOLDERS = ["1_technology", "2_technique", "3_research", "4_tool", "5_concept", "6_prompt", "7_bookmark", "99_other",
           "_obsidian/templates", "_obsidian/attachments", "_obsidian/inbox"]

VAULT_AGENTS = """# AGENTS.md: this vault

Hand-written pentest field notes. The human writes. An agent files, links and checks.

- One note, one idea. Title is the most common name (`sql injection`), never the rare one (`error based sql` is its own atomic note that links up).
- Folder is the type: 1_technology, 2_technique, 3_research, 4_tool, 5_concept, 6_prompt, 7_bookmark, 99_other. Focus is the `domain` property. `web.base` is the web view.
- Frontmatter, always: title, date_created, description, type, domain (list), reference (list of wikilinks). Techniques also carry `attack`.
- Body: flat bullets, under 20 words a line, 3 to 8 bullets, one-word headings (Usage, Detecting, Defense), then an empty `# References`.
- Link while writing. An unknown term becomes a stub link. Do not fill the stub with guesses.
- Short is the rule. Check with `python skills/notes/note_writer/scripts/check_note.py <vault>` (Study-OS).
- Never bulk-rewrite notes. Never delete a note. Never add a screenshot to a short note.
"""


def vault_config(date: str) -> dict[str, object]:
    def rgb(h: str) -> int:
        return int(h.lstrip("#"), 16)
    groups = [("path:2_technique", "#e59aa9"), ("path:5_concept", "#9ec27a"), ("path:4_tool", "#8fb7c9"),
              ("path:1_technology", "#c9b27c"), ("path:3_research", "#a99bd1")]
    return {
        "app.json": {
            "newFileLocation": "folder", "newFileFolderPath": "_obsidian/inbox",
            "attachmentFolderPath": "_obsidian/attachments", "useMarkdownLinks": False,
            "alwaysUpdateLinks": True, "showInlineTitle": True, "propertiesInDocument": "visible",
            "showUnsupportedFiles": False,
        },
        "appearance.json": {"enabledCssSnippets": ["pentest-rice"], "baseFontSize": 16},
        "core-plugins.json": {k: True for k in [
            "file-explorer", "global-search", "switcher", "graph", "backlink", "outgoing-link", "properties",
            "bases", "templates", "command-palette", "outline", "word-count", "file-recovery", "page-preview"]},
        "community-plugins.json": ["new-note-router"],
        "templates.json": {"folder": "_obsidian/templates", "dateFormat": "YYYY-MM-DD"},
        "graph.json": {
            "showOrphans": True, "showTags": False, "hideUnresolved": False, "showAttachments": False,
            "colorGroups": [{"query": q, "color": {"a": 1, "rgb": rgb(c)}} for q, c in groups],
            "nodeSizeMultiplier": 1.1, "linkDistance": 180,
        },
    }


class Writer:
    def __init__(self, dest: Path, dry: bool):
        self.dest, self.dry, self.made, self.kept = dest, dry, [], []

    def put(self, rel: str, data: str | bytes, overwrite: bool = False):
        p = self.dest / rel
        if p.exists() and not overwrite:
            self.kept.append(rel); return
        self.made.append(rel)
        if self.dry: return
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dest"); ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--update-kit", action="store_true", help="overwrite plugin, snippet, templates, bases from the kit")
    a = ap.parse_args()
    dest = Path(a.dest).expanduser().resolve()
    today = datetime.date.today().isoformat()
    w = Writer(dest, a.dry_run)
    kit_over = a.update_kit

    for f in FOLDERS:
        if not a.dry_run: (dest / f).mkdir(parents=True, exist_ok=True)
    for name, cfg in vault_config(today).items():
        w.put(f".obsidian/{name}", json.dumps(cfg, indent=2) + "\n")
    for f in (KIT / "plugin_new_note_router").iterdir():
        w.put(f".obsidian/plugins/new-note-router/{f.name}", f.read_bytes(), kit_over)
    w.put(".obsidian/snippets/pentest-rice.css", (KIT / "snippets/pentest-rice.css").read_bytes(), kit_over)
    for f in (KIT / "templates").iterdir():
        w.put(f"_obsidian/templates/{f.name}", f.read_bytes(), kit_over)
    for f in (KIT / "bases").iterdir():
        w.put(f.name, f.read_bytes(), kit_over)
    w.put("AGENTS.md", VAULT_AGENTS)
    for f in (KIT / "seed").rglob("*.md"):
        text = f.read_text(encoding="utf-8").replace("{{date}}", today)
        w.put(f.relative_to(KIT / "seed").as_posix(), text)

    print(("DRY RUN " if a.dry_run else "") + f"vault: {dest}")
    print(f"wrote {len(w.made)}, kept {len(w.kept)} existing")
    for r in w.made: print("  +", r)
    for r in w.kept: print("  =", r)
    print("next: open the folder as a vault in Obsidian, Settings > Community plugins > turn on community plugins,"
          " enable 'New note router'. Create a note with Ctrl+N.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
