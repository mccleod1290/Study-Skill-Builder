---
name: note_writer
description: >-
  notes skill. writes or trims one pentest note in the short style: one idea, flat bullets,
  most common name as title, rare terms as linked atomic notes, one typed frontmatter. brevity
  and his voice sit on top. first principles and second order add one line, and only where the
  text is ambiguous. use when the user says write a note, add a note, short note, file this in
  the vault, atomic note, trim this note, note this, or /note_writer.
model: inherit
effort: medium
---

# note_writer

One idea in. One short note out. His notes live in `llm_wiki/notes/`, inside the same vault as the LLM wiki (built by `skills/notes/vault_setup`). He owns `notes/`. The LLM wiki owns `wiki/`. The style comes from Helton, grounded in `references/helton_rules.md`.

## The idea (his, from blog 1)

During an engagement he searches `sql injection`, not `error based sql`. So the common word is the entry point and the rare words hang under it.

```text
notes/5_concept/sql injection        <- hub. links only, plus one gist line
   |- notes/2_technique/error based sql     <- atomic. one idea. links back up
   |- notes/2_technique/second order sql
```

Type sets the folder. `domain` sets the focus (`web`). `web.base` shows web notes and web wiki pages together. Five vaults are not needed, and neither is a separate vault from the wiki.

## Steps

0. **Search first.** Look for a note on the same idea (title, then the common name), and for a wiki page of that name. A wiki page with that title: link to it and pick a more specific note title. One name, one file. Found: extend that note, do not write a twin. Not found: continue.
1. **Pick the type and the title.** Types: technology, technique, research, tool, concept, prompt, bookmark, other. Title: the name he would search, lowercase, a bare noun phrase. A rare name is its own atomic note, linked up to its common name.
2. **Write 3 to 8 flat bullets.** Under 20 words a line. One idea per bullet. Define by contrast when it helps: "stored now, run later". Then one-word headings only if needed: Usage, Detecting, Defense. End with `# References`.
3. **Link while writing.** `[[wikilink]]` the first use of every term that has or should have a note. An unknown term stays a stub link. Do not fill a stub with a guess. Stubs are his list of gaps.
   Defences and mitigations are not a type. A defence of one technique is a `# Defense` bullet in that note. A defence with its own life (`samesite cookie`) is a `concept`.
4. **Fill the frontmatter**, always the same: `title, date_created, description, type, domain (list), reference (list of wikilinks)`. Techniques add `attack`. `description` is one line, the gist.
   `reference` may hold a stub. A stub in `reference` is fine: it is a gap marker.
   **Hub link.** A new atomic note adds one bullet to its hub (`- [[new note]]: gist`). That one append is the only edit allowed to an existing note. No hub yet: create the hub as a link-only concept note.
5. **Cut.** Apply `skills/notes/linked/brevity_is_the_soul`: explanation stays, fluff goes. Apply his voice (`skills/notes/linked/writer_skill`): short declaratives, no hype, no hedge.
6. **Ambiguity gate.** Reread each bullet. Only a bullet that would stop him gets a lens, and each lens adds at most one line (lens skills are in `skills/notes/linked/`; run `link_skills.py` once if the folder is empty):
   - law, convention and assumption blur: `first_principles`, one `why:` line
   - a decision or default, and the next event is the lesson: `second_order_thinking`, one `next:` line
   - he must test his own model: `socratic_questions`, live, opt-in
   No ambiguity, no lens. The lens line replaces a weaker line when the note is at budget.
7. **Check.** `python skills/notes/note_writer/scripts/check_note.py <note.md or llm_wiki/notes>`. It must print OK. A note that grew past 120 body words fails. So does a name a wiki page already uses. Cut, do not raise the budget.

## Trimming a long note

Split by idea: one note per idea, each under budget, each linked from the hub. Do not drop content silently. A tip or tool that has no home becomes a stub link (`[[burp csrf poc generator]]`) in the note it came from, or a line in a `3_research` note. Say in the reply what moved where.

## Screenshots

A short note has none. A screenshot goes in a `3_research` note, in `_obsidian/attachments`, only as evidence (output he must keep). Never decorate.

## Do not

- Do not merge two ideas into one note. Split. Link.
- Do not write a monolith like `xyz_day_1`. Do not copy a tool dump into a note. Link the source.
- Do not rewrite his existing notes in bulk. Trim one note when he asks.
- Do not add a quiz or a question list. The Knowledge Check belongs to phase 2 pages only.
- Do not copy Helton's screenshots anywhere public. They are private references in `Artifacts/artifacts/note_vault/helton_refs/`.

The failure is a note that grew a paragraph, a title only he understands, or a lens line on a bullet that had no ambiguity.
