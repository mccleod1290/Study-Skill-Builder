---
name: wiki_lint
description: >-
  llm wiki lint. health check of the private llm_wiki vault: contradictions,
  stale claims, orphan pages, ideas with no page, missing links, data gaps,
  and the next questions and sources to add. use when the user says lint the
  wiki, wiki health, clean my notes, organize my wiki, or /wiki_lint.
model: inherit
effort: high
context: fork
---

# wiki_lint

Read `skills/wiki/SCHEMA.md` first. The vault is `llm_wiki/` in the Study-OS root.

## Checks

1. **Contradictions.** Two pages that claim opposite things. Cite both.
2. **Stale claims.** A claim that a newer source replaces.
3. **Orphans.** A page with no inbound `[[link]]`.
4. **Missing pages.** A `[[link]]` with no page, or an idea named on three or more pages with no page of its own.
5. **Missing links.** Two pages that name each other's idea with no link.
6. **Format.** Properties missing or wrong per SCHEMA.md. Use `skills/obsidian/obsidian-markdown` for the syntax.
7. **Gaps.** Questions the wiki cannot answer that his roadmap needs. Propose sources for each.

## Steps

1. List every page under `llm_wiki/wiki/`. Parse properties and links with a script, not by eye.
2. Run the checks. Fix the mechanical ones (links, properties, index entries).
3. Do not resolve a contradiction by choice. List it for him with both sources.
4. Append the lint line to `llm_wiki/log.md`.

## Output

`llm_wiki/lint_report.md`: the issues, what was fixed, what needs him, the proposed next sources and questions. Report the counts in chat.
