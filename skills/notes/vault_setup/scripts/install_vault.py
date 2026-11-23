#!/usr/bin/env python3
"""install_vault.py: add the notes layer to the vault (the llm_wiki/ folder of Study-OS).

One vault, two owner folders: notes/ is his (hand-written), wiki/ is the LLM's. raw/ is sources.

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
N = "notes"
FOLDERS = [f"{N}/{f}" for f in ["1_technology", "2_technique", "3_research", "4_tool", "5_concept", "6_prompt", "7_bookmark", "99_other",
           "_obsidian/templates", "_obsidian/attachments", "_obsidian/inbox"]]

VAULT_AGENTS = """# AGENTS.md: this vault

One vault, two owners. `notes/` is his hand-written field notes: the LLM reads and links them and never edits them (one exception: `note_writer` appends one bullet to a hub). `wiki/` is the LLM's pages (schema: `skills/notes/wiki/SCHEMA.md` in Study-OS). `raw/` is sources, read only.

Rules for `notes/`:

- One note, one idea. Title is the most common name (`sql injection`), never the rare one (`error based sql` is its own atomic note that links up).
- Folder is the type, inside `notes/`: 1_technology, 2_technique, 3_research, 4_tool, 5_concept, 6_prompt, 7_bookmark, 99_other. Focus is the `domain` property. `web.base` (vault root) is the web view across notes and wiki.
- Frontmatter, always: title, date_created, description, type, domain (list), reference (list of wikilinks). Techniques also carry `attack`.
- Body: flat bullets, under 20 words a line, 3 to 8 bullets, one-word headings (Usage, Detecting, Defense), then an empty `# References`.
- Link while writing. An unknown term becomes a stub link. Do not fill the stub with guesses.
- Short is the rule. Check with `python skills/notes/note_writer/scripts/check_note.py <vault>/notes` (Study-OS). It also fails a note whose name a wiki page already uses: Obsidian resolves a link to one file only.
- A wiki page and a note never share a title. Ingest links to the note, it does not write a twin.
- Never bulk-rewrite notes. Never delete a note. Never add a screenshot to a short note.
"""


def vault_config(date: str) -> dict[str, object]:
    def rgb(h: str) -> int:
        return int(h.lstrip("#"), 16)
    groups = [("path:2_technique", "#e59aa9"), ("path:5_concept", "#9ec27a"), ("path:4_tool", "#8fb7c9"),
              ("path:1_technology", "#c9b27c"), ("path:3_research", "#a99bd1")]
    return {
        "app.json": {
            "newFileLocation": "folder", "newFileFolderPath": "notes/_obsidian/inbox",
            "attachmentFolderPath": "notes/_obsidian/attachments", "userIgnoreFilters": ["raw/"], "useMarkdownLinks": False,
            "alwaysUpdateLinks": True, "showInlineTitle": True, "propertiesInDocument": "visible",
            "showUnsupportedFiles": False,
        },
        "appearance.json": {"enabledCssSnippets": ["pentest-rice"], "baseFontSize": 16},
        "core-plugins.json": {k: True for k in [
            "file-explorer", "global-search", "switcher", "graph", "backlink", "outgoing-link", "properties",
            "bases", "templates", "command-palette", "outline", "word-count", "file-recovery", "page-preview"]},
        "community-plugins.json": ["new-note-router"],
        "templates.json": {"folder": "notes/_obsidian/templates", "dateFormat": "YYYY-MM-DD"},
        "graph.json": {
            "showOrphans": True, "showTags": False, "hideUnresolved": False, "showAttachments": False,
            "colorGroups": [{"query": q, "color": {"a": 1, "rgb": rgb(c)}} for q, c in groups],
            "nodeSizeMultiplier": 1.1, "linkDistance": 180,
        },
    }


class Writer:
    def __init__(self, dest: Path, dry: bool):
        self.dest, self.dry, self.made, self.kept = dest, dry, [], []

    def merge_json(self, rel: str, cfg):
        """Existing config is merged, never replaced: dict keys we need are set, lists are unioned."""
        p = self.dest / rel
        if not p.exists():
            return self.put(rel, json.dumps(cfg, indent=2) + chr(10))
        try:
            cur = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            self.kept.append(rel + " (unreadable json, left alone)"); return
        if isinstance(cur, list) and isinstance(cfg, list):
            new = cur + [x for x in cfg if x not in cur]
        elif isinstance(cur, dict) and isinstance(cfg, dict):
            new = dict(cur)
            for k, v in cfg.items():
                if isinstance(v, list) and isinstance(new.get(k), list):
                    new[k] = new[k] + [x for x in v if x not in new[k]]
                elif k == "colorGroups" or k not in new or new[k] != v:
                    new[k] = v if k != "colorGroups" else new.get(k, v)
        else:
            self.kept.append(rel); return
        if new == cur:
            self.kept.append(rel); return
        self.made.append(rel + " (merged)")
        if not self.dry: p.write_text(json.dumps(new, indent=2) + chr(10), encoding="utf-8")

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
        w.merge_json(f".obsidian/{name}", cfg)
    for f in (KIT / "plugin_new_note_router").iterdir():
        w.put(f".obsidian/plugins/new-note-router/{f.name}", f.read_bytes(), kit_over)
    w.put(".obsidian/snippets/pentest-rice.css", (KIT / "snippets/pentest-rice.css").read_bytes(), kit_over)
    for f in (KIT / "templates").iterdir():
        w.put(f"notes/_obsidian/templates/{f.name}", f.read_bytes(), kit_over)
    for f in (KIT / "bases").iterdir():
        w.put(f.name, f.read_bytes(), kit_over)
    w.put("AGENTS.md", VAULT_AGENTS)
    for f in (KIT / "seed" / "notes").rglob("*.md"):
        text = f.read_text(encoding="utf-8").replace("{{date}}", today)
        w.put("notes/" + f.relative_to(KIT / "seed" / "notes").as_posix(), text)

    print(("DRY RUN " if a.dry_run else "") + f"vault: {dest}")
    print(f"wrote {len(w.made)}, kept {len(w.kept)} existing")
    for r in w.made: print("  +", r)
    for r in w.kept: print("  =", r)
    print("next: open the folder as a vault in Obsidian, Settings > Community plugins > turn on community plugins,"
          " enable 'New note router'. Create a note with Ctrl+N (twice, to test).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
