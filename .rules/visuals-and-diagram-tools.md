# Rule: phase 2 visuals are diagram first, words last

Set by him on 2026-10-16. Source type: log (his words). Applies to every phase 2 visual pass: diagrams, infographics, images. The mechanics are in `skills/phase_2/VISUALS.md` and `skills/phase_2/skills/diagrammer/SKILL.md`.

## 1. Goal

More diagrams, fewer words. A visual must be flashy enough to be remembered and must teach without the paragraph. If a diagram needs its paragraph to make sense, redraw it. Never add words to rescue a weak diagram.

## 2. The three tools

| tool | repo | role | output |
|---|---|---|---|
| `diagram-design` | https://github.com/cathrynlavery/diagram-design | **Lead.** Default for every diagram. 45 types, editorial style, no shadows. | inline SVG |
| `anatomy` | https://github.com/wheresryan22/anatomy | Use when a concept is a mechanism that can be drawn as one physical machine (a lock, a gate, a tumbler). The working of the machine is the concept. | SVG, or one HTML figure |
| `archify` | https://github.com/tt-a1i/archify | **Only when needed.** Use for a whole-system architecture or request path with many parts that the reader must explore (click, trace a path). Never for a flow that `diagram-design` draws well. | one HTML figure |

| `paperbanana` | https://github.com/dwzhu-pku/PaperBanana | **Add-on.** AI-generated academic-style illustrations (ICML 2026 Spotlight). Use when a concept needs a publication-quality figure that the three tools above cannot draw well: complex multi-part research illustrations, annotated mechanism diagrams, academic poster visuals. Runs a 5-agent pipeline (retriever, planner, stylist, visualizer, critic). Needs API key (Gemini or OpenRouter). Ask before using. | PNG or SVG |

Order of choice: `diagram-design` first. Ask for `anatomy` only when a machine metaphor is the clearest teacher. Ask for `archify` last. `paperbanana` is an add-on, never a replacement: use it alongside the others when academic illustration quality is needed.

## 3. The 1:n rule

1. **1**: at most one `archify` diagram per topic folder. The second one is a fail, not a style choice.
2. **n**: as many `diagram-design` and `anatomy` diagrams as the concept needs. A complex concept gets a series: overview, then one diagram per part, then the failure case. Many small diagrams beat one crowded one (at most about 12 boxes each).
3. Every domain of the map has at least one diagram (`phase-order-and-coverage.md`). Extra diagrams are tagged to the node they explain.
4. Each diagram carries `tool` in `phase2_visuals.json`: `diagram-design`, `anatomy`, `archify` or `hand`. `hand` means the tool was not available and the diagram follows the same style rules.

## 4. How the tools are used

1. Read the tool's own `SKILL.md` and style guide from its repo or its installed copy before the first diagram. Do not draw from memory of it.
2. Installing a tool means downloading code. Ask him first and name the repo. Without an install, use the `hand` route: same style, no tool.
3. Output must fit our house: self-contained, no CDN, no web font, no external `src`, theme tokens from `VISUALS.md`, grade and caption in the json. A tool's brand default loses to our tokens.
4. A diagram of an attack names `$TARGET` or a lab host, never a real site (`VISUALS.md`, hard limit 5).
5. The diagram shows the page. It adds no fact, no command, no claim the page does not make.

## 5. Motion

Animation is welcome where order or flow is the point: a packet moving along a path, a state lighting up, a gate opening.

1. CSS or SMIL only, inline in the file. No script in a `.svg`.
2. Motion shows an order or a change of state. It never decorates.
3. `@media (prefers-reduced-motion: reduce)` stops it. `@media print` shows the final frame, with every step visible.
4. Calm: one loop under about 8 seconds, no flashing. Color is never the only signal (`VISUALS.md`, Style rule 4).

## 6. Words

1. A diagram has a title, a caption of one sentence, labels of at most 4 words, and step captions from the page. No paragraph inside a figure.
2. Prefer a diagram over a list, a table of flow, or a paragraph that only sequences events. Keep the sentence that carries a first principle, a condition, or a grade.
3. The explorer adds no prose beyond captions and control labels (`VISUALS.md`, hard limit 3). More diagrams do not raise the page word ceiling. They lower the need for it.

## 7. Check

`python skills/scripts/check_visuals.py <slug> --stage diagrams` must print OK. It fails on a second `archify` diagram, an unknown `tool`, a script in an SVG, or an external source.
