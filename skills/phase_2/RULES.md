# Phase 2 rules

> Overrides, from `.rules/`: deliverables are HTML, PDF only on request (`html-deliverables.md`). Every claim is cited and scored 1 to 5 for confidence (`grounding-and-confidence.md`). Where this file says PDF, produce print-ready HTML. Where it says page count, use words.

**Phase 2 is assimilation.**

The page is how he comes to understand a topic. Depth is how the thing works. Breadth is what it touches. Possibilities are what he can do with it once he sees both. The aim is enough familiarity to do independent work.

The field keeps moving. A page that only quizzes him is useless the month the tool changes. A page that shows the mechanism, the edges, and the ways through is how he stays able to work.

Phase 2 does not test him. No quiz. No workbook. No score. No formal check of his fluency. Three additions, set by him on 2026-11-01:

1. **Knowledge Check.** 3 to 5 short self-assessment questions at the end of the page, in a collapsible section labeled "Knowledge Check." It is homework, not an exam: no grade, no score. Each question has its answer hidden in a toggle. The questions check if he got the gist, not if he memorized the page. A question like "What are the three conditions?" is fine. "Write an exploit" belongs in phase 3.
2. **Tips & Tricks.** A short section of practical gimmicks: shortcuts, one-liners, quick wins, the kind of trick that lets someone who has not spent years on the topic still get the job done. At most 5 to 7 items, each one or two sentences. Pin-on-your-monitor stuff.
3. **Richer visuals and external references.** More inline diagrams, more external reference links to authoritative sources (official docs, research posts, tools). A concept that can be drawn should be drawn. A term that has a canonical reference should link to it.

## Order and coverage

The law is `.rules/phase-order-and-coverage.md`. Phase 2 starts only after phase 1 is complete (map built, build exit 0, the phase 1 agent done), even when he asks for both at once. The page covers every domain, topic and anchor in `phase1_mindmap.json`, each tagged with its node id, in map order. `python skills/scripts/check_coverage.py <slug>` is the check.

## What the page is for

- See the depth of the concept.
- See the breadth around it.
- See the possibilities well enough to start the work alone.
- Keep the references, so a later change in the field has a door back to the source.

## What the page must be

- Up to 5 pages (2500 words) per sub heading. The whole page has no ceiling. Smaller is better. The numbers live in `CRITERIA.md` and `.rules/brevity.md` rule 10.
- References in the last section. A link may also sit where a term would stop him.
- Free of ambiguity. A new term is explained in the flow, or it has an example, a picture, or a link.
- Free of jargon that has no gloss.
- First principles. Second-order only when the next event is the lesson.
- Brevity is the soul. Explanation is not fluff. The flow does not stop.
- Simple language. His writing. The voice spec is `.grok/skills/writer-skill/references/PERSONAL_LANGUAGE_SKILL.md`.

## Where the page comes from

The handoff is `.grok/rules/study-os-handoff.md`.

This phase relies on phase 1. It starts only when `skills/phase_1/output/<slug>/MAP.md` and `TARGET.md` are on disk. Section order is the map order. A domain the map dropped does not get a section. The target is the book, the course, or the work material in `TARGET.md`.

This phase does not read the exam. If the map is missing, stop. Do not invent a curriculum.

## Who does the work

The explainer is an agent. It is not a skill. It runs four agents, in this order, each pass:

1. `ideas_skill` — depth, breadth, possibilities
2. `writer_skill` — his sentences, simple language
3. `reduce_ambiguity` — examples, pictures, links
4. `brevity_is_the_soul` — cut the fluff, keep the flow

Then `frugal_judge` reads `CRITERIA.md` and writes `EVAL.md`. It does not teach, and it does not test him.

If the judge is not satisfied, the explainer runs the four again. No sixth pass.

## The visual pass

Optional. It runs only after the judge says SATISFIED: `diagrammer`, then `web_builder` and `explainer_video`, each in its own agent, then the judge again with the visual checks. It shows the page; it adds no fact and edits nothing above. The law is `VISUALS.md` and `.rules/visuals-and-diagram-tools.md`: more diagrams, fewer words, `diagram-design` leads, `anatomy` for one machine, at most 1 `archify` per topic folder, calm animation allowed.

A quiz, a paper, a build brief, or a spar belongs in `skills/phase_3/`. Not here.
