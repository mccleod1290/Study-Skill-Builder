# Helton's rules, as used here

Sources, both opened 2026-11-23 through a fetch agent, score 4 for the text (a summary of the page, not the raw HTML), score 3 for any claim about what a screenshot shows:

- [Human Memory Management](https://grahamhelton.com/blog/human-memory-management) (2023-10-11). Atomic notes, linking, naming.
- [Human Memory Management and Obsidian V2](https://grahamhelton.com/blog/obsidian-v2) (2026-04-28). Typed frontmatter, type folders, the new-note dialog.

The 45 screenshots from both posts are scored in `Artifacts/artifacts/note_vault/helton_screenshots_scored.md`. The ten best (fewest words) are in `Artifacts/artifacts/note_vault/helton_refs/`. They are his images. They stay private.

## Rules (what he says)

| rule | meaning here |
|---|---|
| atomic | one note per concept, tool or technique. Never one note per training day |
| modular | headings make a note skimmable. Sections can be added or dropped |
| guiding | a note links to sources and to related notes |
| common name for the title | `EDR evasion` is the note. `EDR bypass` links to it |
| link at write time | type `[[x]]` while writing. Do not rely on the backlinks tab |
| stub links are an inventory | an unfilled node on the graph is a gap in knowledge |
| funnel | link to the existing note. Do not re-explain it |
| same schema everywhere | the fields matter less than using them on every note |
| flow keeps notes atomic | the dialog asks for fields, so a note starts structured |
| most notes are short | about 70 percent of his |

## What his short notes show (observed in the screenshots)

Bare lowercase title. Flat bullets, mostly under 20 words. Inline `[[links]]`. Index notes are one link per line. An empty `# References` heading ends the note. One-word headings (Usage, Detecting, Defense, Attacking). No screenshot or terminal dump in a short note.

## Negative examples (from his own post)

An awk wall of nested bullets. A Notion page with long paragraphs hidden in toggles. A Kubernetes note with kubectl output in the middle. A Rubeus note with several ideas and many images. Each fails "atomic" or "short".

## What this vault changes

| his | here | why |
|---|---|---|
| five vaults | one vault, `domain` property, `web.base` | web stays one click away |
| `domain` list incl. career, redteam | same, plus `web`, `cloud`, `ai` first | his focus is web |
| ATT&CK tag on techniques | `attack` field takes ATT&CK, CWE or OWASP id | web techniques map to CWE |
| custom publishing plugins | none | not needed |
