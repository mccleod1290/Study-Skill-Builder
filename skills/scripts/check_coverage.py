#!/usr/bin/env python3
"""check_coverage.py: does phase2_page.md cover every node of phase1_mindmap.json?
Usage: python skills/scripts/check_coverage.py <slug> [--scope d1,C1.*]
Rule: .rules/phase-order-and-coverage.md. Exit 1 on any missing or unknown id, or wrong order.
Tags in the page are node ids in curly braces: {d1}, {d1a}, {H1}, {C1.1}.
--scope: a run that writes only part of the map (one domain at a time). Comma list of ids or
glob patterns. A domain id brings its whole subtree. Anchors are checked only when named or
matched (C1.*), because one topic can feed anchors of other domains. Map ids outside the scope
are not unknown. Order is checked inside the scope."""
import fnmatch, json, re, sys, pathlib

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / ".rules").is_dir())

def nodes(n, out):
    for c in n.get("k", []):
        out.append(c["id"]); nodes(c, out)
    return out

def subtree(n, want, out, inside=False):
    for c in n.get("k", []):
        hit = inside or c["id"] in want
        if hit: out.append(c["id"])
        subtree(c, want, out, hit)
    return out

def main():
    args = sys.argv[1:]
    scope = None
    if "--scope" in args:
        i = args.index("--scope")
        if i + 1 >= len(args):
            print("ERROR: --scope needs a value, e.g. --scope d1,C1.*"); return 1
        scope = [s.strip() for s in args[i + 1].split(",") if s.strip()]
        del args[i:i + 2]
    slug = args[0] if args else ""
    hits = sorted((ROOT / "Artifacts" / "artifacts").glob("**/" + slug + "/phase1_mindmap.json")) if slug else []
    if not hits:
        print("ERROR: no phase1_mindmap.json for slug", repr(slug)); return 1
    folder = hits[0].parent
    page = folder / "phase2_page.md"
    if not page.is_file():
        print("ERROR: missing", page); return 1
    m = json.loads(hits[0].read_text(encoding="utf-8"))
    all_ids = nodes(m["tree"], [])
    all_anchors = list(m.get("controls", {}))
    ids, anchors = all_ids, all_anchors
    if scope:
        pat = [s for s in scope if any(ch in s for ch in "*?[")]
        lit = set(scope) - set(pat)
        bad = sorted(lit - set(all_ids) - set(all_anchors))
        if bad:
            print("ERROR: --scope ids not in the map:", ", ".join(bad)); return 1
        want = lit | {i for i in all_ids if any(fnmatch.fnmatchcase(i, p) for p in pat)}
        ids = subtree(m["tree"], want, [])
        anchors = [a for a in all_anchors if a in lit or any(fnmatch.fnmatchcase(a, p) for p in pat)]
        if not ids and not anchors:
            print("ERROR: --scope matches nothing in the map:", ",".join(scope)); return 1
    text = re.sub(r"```.*?```", "", page.read_text(encoding="utf-8"), flags=re.S)
    tags = re.findall(r"\{([A-Za-z]+\d+(?:\.\d+)?[a-z]?)\}", text)
    seen = set(tags)
    missing = [i for i in ids + anchors if i not in seen]
    unknown = sorted(seen - set(all_ids) - set(all_anchors))
    first = {}
    for pos, t in enumerate(tags):
        first.setdefault(t, pos)
    order = [i for i in ids if i in first]
    bad_order = [b for a, b in zip(order, order[1:]) if first[b] < first[a]]
    for x in missing: print("MISSING", x)
    for x in unknown: print("UNKNOWN", x)
    for x in bad_order: print("ORDER  ", x, "appears before an earlier node")
    if missing or unknown or bad_order:
        print(f"FAIL  {len(missing)} missing, {len(unknown)} unknown, {len(bad_order)} out of order"); return 1
    where = f" (scope {','.join(scope)})" if scope else ""
    print(f"OK  {len(ids)} nodes and {len(anchors)} anchors covered, in map order{where}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
