#!/usr/bin/env python3
"""Turn the bibtex2html publication lists into Jekyll pages that use the
site layout. Run after bibtex2html (bib2html.sh calls it at the end)."""
import re
from pathlib import Path

LISTS = {
    "publication-book": "Authored Books",
    "publication-journal": "Refereed Journal Articles",
    "publication-conf": "Conference Papers",
    "publication-chapter": "Book Chapters",
}



def nav(current):
    links = ['<a href="/publications/"><i class="fas fa-arrow-left" aria-hidden="true"></i> All publications</a>']
    for name, title in LISTS.items():
        attr = ' class="is-current" aria-current="page"' if name == current else ""
        links.append(f'<a href="{name}.html"{attr}>{title}</a>')
    return '<nav class="pub-jump" aria-label="Publication lists">\n  ' + "\n  ".join(links) + "\n</nav>"


here = Path(__file__).resolve().parent
for name, title in LISTS.items():
    path = here / f"{name}.html"
    html = path.read_text(encoding="utf-8")
    if html.startswith("---"):
        continue  # already wrapped
    table = re.search(r"<table>.*</table>", html, re.S).group(0)
    # award labels added by bib2html.sh -> site badges
    table = re.sub(
        r'<b style="color:red;">\((.*?)\)</b>',
        r'<span class="badge badge--award">\1</span>',
        table,
    )
    table = table.replace("Yi&nbsp;Mei", "<b>Yi&nbsp;Mei</b>")
    count = table.count('class="bibtexitem"')
    path.write_text(
        f"""---
layout: archive
title: "{title}"
permalink: /publications/{name}.html
author_profile: true
share: false
comments: false
---

{nav(name)}

<p>{count} items. If you need the PDF of any paper, please <a href="mailto:yi.mei@ecs.vuw.ac.nz">contact me</a>.</p>

<div class="bib-list">
{{% raw %}}
{table}
{{% endraw %}}
</div>
""",
        encoding="utf-8",
    )
    print(f"wrapped {path.name} ({count} items)")
