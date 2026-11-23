---
name: vault_setup
description: >-
  notes skill. builds or tops up the pentest Obsidian vault: type folders, one frontmatter
  schema, templates, the web and all Bases, the new-note router plugin (asks type, name,
  domain, references, then files the note), a calm CSS snippet, and a few seed notes. never
  overwrites a file. use when the user says set up the vault, build the obsidian vault, new
  vault, rice my obsidian, new note dialog, new note automation, or /vault_setup.
model: inherit
effort: medium
disable-model-invocation: true
---

# vault_setup

Side effects: it writes a folder. Show the dry run first. It never overwrites a file and never deletes.

## Steps

1. Dry run: `python skills/notes/vault_setup/scripts/install_vault.py <dest> --dry-run`. Read the list.
2. Install: same command without `--dry-run`. Default destination: `Documents/Pentest Vault`. Do not point it at an existing vault with notes unless he says so. His existing vaults stay untouched.
3. Check the plugin logic: `node skills/notes/vault_setup/tests/test_router.js` must print `OK router core`.
4. Check the seed notes: `python skills/notes/note_writer/scripts/check_note.py <dest> --stubs` must print OK.
5. Tell him the two manual steps Obsidian needs: open the folder as a vault, then Settings > Community plugins > turn on community plugins > enable New note router. Obsidian asks for this once per vault. A script cannot answer it.
6. Kit update later: add `--update-kit`. It refreshes the plugin, snippet, templates and bases only.

## What is in the kit (`assets/`)

| path | job |
|---|---|
| `plugin_new_note_router/` | the dialog. Local code, no network, no download |
| `snippets/pentest-rice.css` | fonts, colours, compact properties. Unknown links glow rose, so stubs show |
| `templates/` | one body skeleton per type. The plugin applies it. The frontmatter comes from the dialog |
| `bases/web.base`, `all.base` | the web view, plus orphans and notes with no gist |
| `seed/` | `sql injection` hub and four atomic techniques, as the pattern to copy |

## How the dialog works

New note (Ctrl+N) lands in `_obsidian/inbox`. The plugin sees an empty new note, then asks: type, name, domain (many, `Done selecting` ends), for a technique an `attack` id (free text, optional), references (many, optional). It writes the frontmatter, applies the template, moves the note to its type folder, opens it. Cancel at any step: the note stays in the inbox, untouched. Name clash: nothing changes. Command palette: `Route this note` runs the same flow on the open note. Pasted, synced or imported notes are not empty, so they are never interrupted.

## Limits (say them)

- The plugin core is tested in node. The modal flow needs Obsidian. It was not run in the app in the session that built it. First real test: Ctrl+N in the new vault.
- The font list falls back to Consolas if JetBrains Mono, Cascadia Code and Fira Code are missing.
- A community theme was not installed. That is a download, so it needs his yes.

## Do not

- Do not install a community plugin or theme without asking.
- Do not move or rewrite notes in his other vaults. A migration is a separate job.
