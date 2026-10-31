#!/usr/bin/env python3
"""Rewrite the activity block in README.md from solomonsmith.dev/activity.json.

The JSON is built weekly from the GitHub API by the portfolio repo. This
script only reformats it; it adds no text of its own beyond labels.
"""

import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

SOURCE = "https://solomonsmith.dev/activity.json"
README = Path(__file__).resolve().parents[2] / "README.md"
START, END = "<!-- activity:start -->", "<!-- activity:end -->"


def plural(n, word):
    return f"{n} {word}{'' if n == 1 else 's'}"


def render(w):
    start, end = date.fromisoformat(w["week_start"]), date.fromisoformat(w["week_end"])
    t = w["totals"]
    lines = [f"**{start:%b} {start.day} to {end:%b} {end.day}, {end.year}:** "
             f"{plural(t['commits'], 'commit')}, {plural(t['prs'], 'merged PR')}, "
             f"{plural(t['releases'], 'release')} across {plural(t['repos'], 'repo')}.", ""]
    for r in w["repos"]:
        name = f"[{r['name']}]({r['url']})" if r["url"] else r["name"]
        parts = [plural(r["commits"], "commit")]
        if r["prs"]:
            parts.append(plural(len(r["prs"]), "merged PR"))
        if r["releases"]:
            parts.append("released " + ", ".join(x["tag"] for x in r["releases"]))
        lines.append(f"- {name}{' (new)' if r['new'] else ''}: {', '.join(parts)}")
    if p := w.get("private"):
        lines.append(f"- Private work: {plural(p['repos'], 'repo')}, {plural(p['commits'], 'commit')}"
                     + (f", {plural(p['prs'], 'merged PR')}" if p["prs"] else ""))
    if not w["repos"] and not w.get("private"):
        lines.append("No GitHub activity this week.")
    lines += ["", "Updated every Monday from the GitHub API. Full log: [solomonsmith.dev/log](https://solomonsmith.dev/log/)"]
    return "\n".join(lines)


def main():
    with urllib.request.urlopen(SOURCE, timeout=30) as resp:
        week = json.load(resp)
    text = README.read_text()
    if START not in text or END not in text:
        sys.exit("README.md is missing the activity markers")
    block = f"{START}\n{render(week)}\n{END}"
    README.write_text(re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S))


if __name__ == "__main__":
    main()
