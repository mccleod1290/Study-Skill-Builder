# Page order

Replaces `ideas_skill` (archived 2026-11-23, `skills/_archive/ideas_skill/ARCHIVED.md`). His steer: the lenses `first_principles` and `second_order_thinking` do the thinking. They run only where the text is ambiguous. Nothing else decides the order.

## Draft rule (writer_skill, first pass)

1. Read `skills/phase_1/output/<slug>/MAP.md`. Missing file: stop, write nothing.
2. Every node of `phase1_mindmap.json` gets a place, tagged `{d1}`, `{d1a}`, `{H1}`. A topic can be one line. It cannot be missing. Rule: `.rules/phase-order-and-coverage.md`.
3. Section order is map order. A domain the map dropped gets no section. Do not reteach an acquired skill. Exposure is not acquired.
4. Each learning section, in this order: the parts the result depends on, the condition, when it does not apply, then how. A page that opens with the procedure fails.
5. Claims come from `SOURCES.md`. A line with no opened url stays off the page.
6. No quiz, workbook or question block (the Knowledge Check at the end is the one exception, see `RULES.md`).

## Lens gate (the ambiguity rule)

`reduce_ambiguity` marks each spot where a new learner stumbles. It writes the marks to `phase2_ambiguity.md`: node id, the stuck line, and which lens it needs. Lenses run on marked nodes only. A node with no mark gets no lens, no extra line.

| mark | lens | adds to the page |
|---|---|---|
| claim unclear: law, convention or assumption mixed | `first_principles` | one why line. The worksheet stays in `phase2_fp.md` |
| decision or default, next event is the lesson | `second_order_thinking` | one next-event line. The chain stays in `phase2_so.md` |
| the learner must test his own model | `socratic_questions` (opt-in) | one question, asked in the live chat. Nothing on the page |

A lens adds at most one line to a node. It never grows a section. `brevity_is_the_soul` runs last and cuts it if the line does not earn its place.

## Loop

```text
writer_skill -> reduce_ambiguity -> lenses (marked nodes only) -> brevity_is_the_soul -> frugal_judge
```
Not satisfied: run again, cap 3, 4 or 5.
