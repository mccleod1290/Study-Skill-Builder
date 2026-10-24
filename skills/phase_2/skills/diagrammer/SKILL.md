---
name: diagrammer
description: >-
  phase 2 visual pass, step 1. turns a judged phase 2 page into hand-drawn
  inline svg diagrams, one per domain and more where the order or the shape is
  the point, and writes phase2_visuals.json for web_builder and
  explainer_video. a diagram shows the page, it adds no fact. use when the
  page is SATISFIED and the user says diagrams, draw it, diagram this,
  visual pass, or /diagrammer.
model: inherit
effort: high
---

# diagrammer

Karpathy's second rung: a diagram is often easier to take in than prose. Shared rules, file names, style tokens and the json shape: `skills/phase_2/VISUALS.md`. Read it first.

## Gate

`phase2_eval.md` says SATISFIED and `check_coverage.py <slug>` prints OK. If not, draw nothing and say so.

## Tools

Law: `.rules/visuals-and-diagram-tools.md`. Read it with VISUALS.md.

1. `diagram-design` leads. Read its `SKILL.md` and `references/style-guide.md` first, pick its diagram type, then output inline SVG in our tokens.
2. `anatomy` when the concept is one mechanism that a machine shows best. Read its `SKILL.md` first.
3. `archify` only when the reader must explore a whole system. At most 1 per topic folder.
4. 1:n: one archify at most, n of the others. A complex concept gets a series, not one crowded drawing.
5. Tool not installed: do not install it. Say so in the reply and draw `tool: "hand"` in the same style.
6. Animate order and flow where it helps. CSS or SMIL, calm, `prefers-reduced-motion` off, print shows the last frame.
7. Few words. Labels at most 4 words. The diagram teaches, the page text stays the source.

## Choose what to draw

Read `phase2_page.md` and `phase1_mindmap.json`. Every domain gets at least one diagram. A topic or an anchor gets one only when one of these is true:

| the page shows | kind | draw |
|---|---|---|
| an order of events between parties | `sequence` | lanes for browser, proxy, app, store. arrows in time order. |
| a decision or a pipeline | `flow` | boxes and diamonds. the bad branch red and dashed. |
| who trusts whom | `boundary` | a dashed line where trust changes. what crosses it. |
| a thing that changes state | `state` | states and the event on each edge. |
| 2011 against 2026, or two tools | `compare` | two columns, same rows. |
| the parts of a request, URL or token | `anatomy` | the real string, each part bracketed and named. |
| a whole system the reader explores | `system` | archify only. one per folder. |
| one mechanism as a machine | `machine` | anatomy only. the machine's working is the concept. |

A diagram that only repeats a list is not a diagram. Skip it.

## Draw

1. Hand-write the SVG. Use the tokens and the five rules in VISUALS.md, Style.
2. Use the exact names, headers, parameters and commands of the page. Do not invent an endpoint. Hosts are `$TARGET` or a lab host.
3. Where the page gives an order, wrap each step in `<g data-step="n">`, n from 1. `steps` in the json gets one caption per step, the page's own words cut short.
4. Where the page gives the condition and when it does not apply, wrap the two in `<g data-when="applies">` and `<g data-when="fails">`. `when` in the json gets one line each.
5. Grade: the lowest grade of the claims you drew. A grade 2 claim is drawn grey and labelled "not verified".
6. Small and legible: at most about 12 boxes. If it needs more, it is two diagrams.

## Write

- `diagrams/<id>.svg` or `.html`, one file each. `<node_id>_<n>` for more than one diagram of a node.
- `phase2_visuals.json` with `page_hash` = sha256 of `phase2_page.md`.

## Check

`python skills/scripts/check_visuals.py <slug> --stage diagrams` prints OK.

## Do not

- Edit the page, the map, or any other skill's output.
- Draw an image with a raster, a web font, or a link to a CDN.
- Add a claim the page does not make. A gap you see goes in your reply, not in the drawing.

## Model

model: inherit. effort: high. The failure is a pretty diagram that says something the page does not.
