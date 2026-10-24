---
name: wiki_ingest
description: >-
  llm wiki ingest. takes one source (a study artifact, an article, notes, a lab
  writeup) into the private llm_wiki vault: a source page, new or updated
  concept, connection, mental model and example pages, index and log. use when
  the user says ingest, add to wiki, file this, put this in my wiki, update the
  wiki, or /wiki_ingest.
model: inherit
effort: medium
---

# wiki_ingest

Read `skills/wiki/SCHEMA.md` first. It is the contract for the vault at `llm_wiki/`.

## Inputs

One source: a path under `llm_wiki/raw/`, a Study-OS artifact under `Artifacts/artifacts/<slug>/`, or a file he names. One source per run, so he can follow the change. If no source is named, stop and ask.

## Steps

1. If `llm_wiki/` does not exist, create the layout in SCHEMA.md with an empty `index.md` and `log.md`.
2. Read the source in full. Read `llm_wiki/index.md`.
3. Tell him the 3 to 5 main takeaways in chat. Wait for a correction only if he gives one.
4. Write `wiki/sources/<source-slug>.md`: summary, what it claims, the grade of each claim.
5. For each idea: update its page in `concepts/`, `mental_models/` or `examples/`, or create it. Merge, do not duplicate. When the new source contradicts a page, keep both claims, mark the conflict with a `> [!warning]` callout, and cite both.
6. Write a `connections/<a>--<b>.md` page only when the shared mechanism is real and stated.
7. Add `[[wikilinks]]` both ways.
8. Rebuild `index.md`. Append one line to `log.md` in the SCHEMA.md format.

## Output

Pages under `llm_wiki/wiki/`, `llm_wiki/index.md`, `llm_wiki/log.md`. Report in chat: the pages created, the pages changed, the conflicts.

## Do not

- Do not edit anything in `llm_wiki/raw/` or `user-input-learning-text/`.
- Do not mark a topic `solved` from a source. Only his own lab result moves status.
- Do not copy wiki pages anywhere outside `llm_wiki/`. The vault is private.
