#!/usr/bin/env python3
"""distill.py: a DeepSeek Harness trajectory export -> reasoning_all.html + reasoning_steps.json.

Usage: python distill.py <trajectory.json> <out_dir>

Reads the harness "Download session log" JSON. The exact shape varies by harness
version, so the parser is tolerant: it walks the tree and pulls every assistant
reasoning step and the tool calls near it. It records all reasoning; it does not
judge gaps. The gap pass is the agent's job (see SKILL.md), because that needs
the skill text, not just the log.
"""
from __future__ import annotations
import html
import json
import sys
from pathlib import Path

# field names seen across harness versions; matched case-insensitively
REASON_KEYS = ("thinking", "reasoning", "reasoning_content", "thought", "analysis")
TEXT_KEYS = ("content", "text", "message", "summary")
TOOL_KEYS = ("tool", "tool_call", "tool_calls", "function", "command")


def is_assistant(obj: dict) -> bool:
    role = str(obj.get("role") or obj.get("type") or obj.get("author") or "").lower()
    return "assist" in role or role in ("model", "ai")


def as_text(v) -> str:
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return "\n".join(as_text(x) for x in v if x)
    if isinstance(v, dict):
        for k in TEXT_KEYS:
            if k in v:
                return as_text(v[k])
    return ""


def walk(node, steps: list, turn=[0]):
    """Collect assistant reasoning and tool calls in document order."""
    if isinstance(node, dict):
        reason = next((as_text(node[k]) for k in node if k.lower() in REASON_KEYS and node[k]), "")
        tools = []
        for k in node:
            if k.lower() in TOOL_KEYS and node[k]:
                tools.append(node[k])
        if is_assistant(node) and (reason or any(k.lower() in TEXT_KEYS for k in node)):
            turn[0] += 1
            steps.append({
                "n": turn[0],
                "reasoning": reason,
                "say": as_text({k: node[k] for k in node if k.lower() in TEXT_KEYS}),
                "tools": [summarize_tool(t) for t in tools],
            })
        for v in node.values():
            walk(v, steps, turn)
    elif isinstance(node, list):
        for v in node:
            walk(v, steps, turn)


def summarize_tool(t) -> str:
    if isinstance(t, list):
        return "; ".join(summarize_tool(x) for x in t)
    if isinstance(t, dict):
        name = t.get("name") or t.get("tool") or t.get("function") or "tool"
        arg = t.get("command") or t.get("arguments") or t.get("input") or ""
        return f"{name}: {as_text(arg)[:300]}"
    return str(t)[:300]


def esc(s: str) -> str:
    return html.escape(s or "")


def render(steps: list) -> str:
    rows = []
    for s in steps:
        tools = "".join(f"<li><code>{esc(t)}</code></li>" for t in s["tools"])
        rows.append(
            f'<section class="step"><h3>Step {s["n"]}</h3>'
            + (f'<div class="reason"><b>Reasoning</b><pre>{esc(s["reasoning"])}</pre></div>' if s["reasoning"] else "")
            + (f'<div class="say"><b>Said</b><pre>{esc(s["say"])}</pre></div>' if s["say"] else "")
            + (f'<div class="tools"><b>Tool calls</b><ul>{tools}</ul></div>' if tools else "")
            + "</section>"
        )
    return (
        "<!doctype html><html lang=en><head><meta charset=utf-8>"
        "<meta name=viewport content='width=device-width,initial-scale=1'>"
        "<title>Trajectory: all assistant reasoning</title><style>"
        "body{font:15px/1.5 system-ui,sans-serif;max-width:820px;margin:2rem auto;padding:0 1rem;color:#111}"
        ".step{border-top:1px solid #ddd;padding:1rem 0}h3{margin:.2rem 0;color:#555}"
        "pre{white-space:pre-wrap;background:#f6f6f6;padding:.6rem;border-radius:6px;overflow-wrap:anywhere}"
        ".reason pre{background:#eef4ff}code{word-break:break-all}"
        "@media(prefers-color-scheme:dark){body{background:#111;color:#eee}pre{background:#1d1d1d}.reason pre{background:#14243f}}"
        "</style></head><body><h1>All assistant reasoning</h1>"
        f"<p>{len(steps)} assistant steps, in order, from the harness trajectory export.</p>"
        + "".join(rows) + "</body></html>"
    )


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    data = json.loads(src.read_text(encoding="utf-8"))
    steps: list = []
    walk(data, steps)
    if not steps:
        print("WARN: no assistant steps found. Check the export shape; adjust REASON_KEYS/role matching.")
    out.mkdir(parents=True, exist_ok=True)
    (out / "reasoning_steps.json").write_text(json.dumps(steps, indent=2), encoding="utf-8")
    (out / "reasoning_all.html").write_text(render(steps), encoding="utf-8")
    print(f"wrote {len(steps)} steps to {out/'reasoning_all.html'} and reasoning_steps.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
