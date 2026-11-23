# First principles worksheet: <slug>

Pair: run this first. `second_order_thinking` then says what follows (`phase2_so.md`). Both files use the same `node id`. `second_order_thinking` should take its `no: base` test (below g3) from `base grade` in this file, not from `grade`.

Opened sources: <name, url, accessed (ISO date)>. Not opened: <name>.
Tally of parts by grade: 5 = <n>, 4 = <n>, 3 = <n>, 2 = <n>, 1 = <n>. Weak spots first: <part ids at grade 1 or 2>.

How to fill (delete this block when done):
- One row per node of the map, in map order. No node is dropped.
- A node that fails the gate gets a short row. `rebuild (how)` starts with `gate: analogy`. Its copied convention and its carry-over assumption each get a row in the Parts table, with a grade.
- A node that is not a claim gets a one-line row: `rebuild (how)` starts with `gate: not a claim`, `parts` says none, there is no Parts-table row, and both grade cells say n/a.
- Column order follows the page order set in `PAGE_ORDER.md`: parts, condition, when it does not apply, then how. Keep the columns in this order.
- `node id` is the map id (`d1a`). A claim typed in chat has no map: `chat1`.
- `parts` lists part ids by kind. Each part has a row in the Parts table.
- `grade` is the weakest grade among all the node's parts. Grades run 1 to 5, higher is better (`.rules/grounding-and-confidence.md`). A law with no evidence is an assumption, grade 2, "not verified".
- `base grade` is the weakest grade among the law and convention parts the rebuild stands on. An assumption is a test to run, so it does not lower `base grade`. A gate row has a copied convention, so it takes that convention's grade. A node with no law or convention part takes the grade of its stop. Why: one untested assumption sets `grade` to 2 or 1, and `second_order_thinking` would then chain nothing.
- `evidence`: add `so: yes` when the next event is the lesson. The chain itself belongs to `second_order_thinking`.
- A cell is short. The writer owns the length.

## Nodes

| node id | claim as stated | parts | evidence | grade | base grade | condition | when it does not apply | rebuild (how) |
|---|---|---|---|---|---|---|---|---|
| <d1a> | <the claim in one sentence, as the source or the user stated it> | law <L1>; convention <C1, C2>; assumption <A1> | <the source to open first, or the cheapest test of the weakest part> | <1 to 5> | <1 to 5> | <the context where the parts hold: what, for whom, which version> | <where the claim fails, where analogy is the better tool, the flip signal> | <1 what must be true. 2 the cheapest set. 3 the gap to the analogy answer> |

## Parts

| node id | part id | kind | part | holder | evidence | grade |
|---|---|---|---|---|---|---|
| <d1a> | <L1> | law | <one plain sentence, true in this context> | n/a | <source and section, or the measurement or calculation you ran> | <1 to 5> |
| <d1a> | <C1> | convention | <what is held> | <who holds it> | <source and section> | <1 to 5> |
| <d1a> | <A1> | assumption | <what nobody tested. An "I do not know" goes here as an open question, grade 1> | n/a | <the cheapest test> | <1 to 5> |

## Stops

| node id | chain ended at | stop kind | why it stopped there |
|---|---|---|---|
| <d1a> | <the last answer> | <law, measurement or I do not know> | <one sentence> |
