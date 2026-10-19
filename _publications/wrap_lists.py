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

NAV = " · ".join(
    f'<a href="{name}.html">{title}</a>' for name, title in LISTS.items()
)

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

<nav class="pub-jump"><a href="/publications/">← All publications</a> · {NAV}</nav>

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
