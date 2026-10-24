---
name: wiki_query
description: >-
  llm wiki query. answers a question from the private llm_wiki vault with
  citations to its pages, and files a good answer back as a new page so the
  work compounds. use when the user says ask my wiki, what do I know about,
  search my notes, from my wiki, or /wiki_query.
model: inherit
effort: medium
---

# wiki_query

Read `skills/wiki/SCHEMA.md` first.

## Steps

1. Read `llm_wiki/index.md`. Pick the pages that bear on the question.
2. Read those pages and follow their links one level.
3. Answer. Cite each claim as `[[page]]` and keep its grade. Say what the wiki does not cover. Do not fill a gap from memory without saying so.
4. Choose the form: a short answer in chat, a comparison table, or an HTML page under `Artifacts/artifacts/<slug>/` for a long one.
5. If the answer is new synthesis that he will want again, file it as a page in `llm_wiki/wiki/` (usually `concepts/` or `connections/`), update `index.md`, and log it.
6. Append the query line to `log.md`.

## Do not

- Do not answer from the raw sources when the wiki has the page. Use the wiki first.
- Do not send wiki content to any outside service or into the public export.
