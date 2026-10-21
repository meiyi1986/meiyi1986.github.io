#!/usr/bin/env python3
"""Derive the site's stats and counts from their sources and write
_data/stats.json, which the pages read as site.data.stats.

Sources:
  _pages/grantsawards.md   funding totals, award counts
  _pages/services.md       editor roles, Outstanding AE count, journals reviewed
  _pages/supervision.md    student counts
  _pages/teaching.md       courses taught and coordinated
  _publications/*.bib      publication counts
  OpenAlex API             citation counts for highlighted papers (DOIs below
                           and every DOI linked from a pub-feature card on the
                           Publications page); previous values are kept if the
                           API cannot be reached.

Run from the repository root:  python3 _scripts/update_stats.py
The deploy workflow runs it before every build.
"""
import datetime
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "_pages"
OUT = ROOT / "_data" / "stats.json"

# extra DOIs whose citation counts are quoted on the research theme pages
EXTRA_DOIS = ["10.1109/TEVC.2013.2281543", "10.1109/TEVC.2022.3225509"]


def read(name):
    """Page text with HTML comments removed, so commented-out entries are not counted."""
    return re.sub(r"<!--.*?-->", "", (PAGES / name).read_text(encoding="utf-8"), flags=re.S)


def section(text, start, end=None):
    i = text.index(start)
    j = text.find(end, i + len(start)) if end else -1
    return text[i:j if j != -1 else None]


def strip(s):
    return re.sub(r"<[^>]+>", "", s).strip()


def money(v):
    if v >= 1e6:
        m = v / 1e6
        s = f"{int(m * 10) / 10:g}M"
    elif v >= 1e3:
        s = f"{int(v / 1e3)}K"
    else:
        s = str(int(v))
    return "$" + s


def plus(n):
    """Round down to a readable figure with a plus sign: 746 -> '740+'."""
    if n >= 10000:
        return f"{n // 1000 * 1000:,}+"
    if n >= 1000:
        return f"{n // 100 * 100:,}+"
    if n >= 100:
        return f"{n // 10 * 10}+"
    return str(n)


# ---------------------------------------------------------------- grants & awards
def grants_awards():
    t = read("grantsawards.md")
    grants = re.findall(r"<li>.*?</li>", section(t, "## Grants", "## Awards"), re.S)
    pi_total, theme = 0, 0
    for g in grants:
        amt = re.search(r'badge--amount">\$([\d,]+) NZD', g)
        role = re.findall(r'<span class="badge">([^<]+)</span>', g)
        if not amt:
            continue
        v = int(amt.group(1).replace(",", ""))
        if any(r.strip() in ("PI", "Sole PI") for r in role):
            pi_total += v
        if any("Theme Leader" in r for r in role):
            theme = max(theme, v)
    awards = re.findall(r'badge--award">([^<]+)<', section(t, "## Awards"))
    paper = [a for a in awards if re.fullmatch(r"(Best|Outstanding)( Student)? Paper Award", a.strip())]
    excellence = [a for a in awards if "Research Excellence Award" in a]
    return {"grants": len(grants), "pi_funding": money(pi_total) + ("+" if pi_total % 100000 else ""),
            "pi_funding_nzd": pi_total, "theme_leader_funding": money(theme),
            "awards": len(awards), "paper_awards": len(paper), "research_excellence_awards": len(excellence)}


# ---------------------------------------------------------------- services
def services():
    t = read("services.md")
    ed = section(t, "## Editorship", "## ")
    roles = re.findall(r"<li><strong>(Editor|Associate Editor)</strong>", ed)
    oae = re.findall(r"Outstanding Associate Editor \d{4}", ed)
    rev = section(t, "## Journal Reviewer", "## Membership")
    pc = section(t, "## Conference Program Committee Member", "## Journal Reviewer")
    org = section(t, "## Conference Organisation", "## Conference Program Committee Member")
    return {"editor_roles": len(roles), "outstanding_ae": len(oae),
            "journals_reviewed": len(re.findall(r"<li>", rev)),
            "pc_conferences": len(re.findall(r"<li>", pc)),
            "organising_roles": len(re.findall(r"<li>", org))}


# ---------------------------------------------------------------- supervision
def supervision():
    t = read("supervision.md")

    def count(sec, sub=None):
        s = section(t, sec, "\n## ")
        if sub:
            s = section(s, sub, "\n### ")
        return len(re.findall(r"<li>", s))
    phd_cur, phd_grad = count("## PhD", "### Current"), count("## PhD", "### Graduated")
    vis = count("## Visiting PhD")
    hon, summ = count("## Honours"), count("## Summer")
    ms_cur, ms_grad = count("## Masters", "### Current"), count("## Masters", "### Graduated")
    return {"phd_current": phd_cur, "phd_graduated": phd_grad, "visiting_phd": vis,
            "masters_current": ms_cur, "masters_graduated": ms_grad,
            "honours": hon, "summer": summ, "honours_summer": hon + summ}


# ---------------------------------------------------------------- teaching
def teaching():
    t = read("teaching.md")
    years = [int(y) for y in re.findall(r'teaching-year__year">(\d{4})<', t)]
    codes = set()
    for prefix, num, more in re.findall(r"\(([A-Z]{4})(\d{3})((?:/\d{3})*)\)", t):
        codes.add(prefix + num)
        codes.update(prefix + n for n in re.findall(r"\d{3}", more))
    coord = re.findall(r'<span class="badge">[^<]*Coordinator</span>', section(t, "## Courses"))
    return {"courses": len(codes), "coordinated": len(coord),
            "first_year": min(years) if years else None, "latest_year": max(years) if years else None}


# ---------------------------------------------------------------- publications
def publications():
    out = {}
    for kind, f in [("journal", "publication-journal.bib"), ("conference", "publication-conf.bib"),
                    ("book", "publication-book.bib"), ("chapter", "publication-chapter.bib")]:
        out[kind] = len(re.findall(r"^\s*@\w+\s*\{", (ROOT / "_publications" / f).read_text(encoding="utf-8"), re.M))
    out["total"] = sum(out.values())
    return out


# ---------------------------------------------------------------- citations
def citations(previous):
    dois = set(d.lower() for d in EXTRA_DOIS)
    dois.update(d.lower() for d in re.findall(r'pub-feature__title"><a href="https://doi.org/([^"]+)"', read("publications.md")))
    out, raw = dict(previous.get("citations", {})), dict(previous.get("citations_raw", {}))
    fetched = 0
    for doi in sorted(dois):
        url = f"https://api.openalex.org/works/doi:{doi}?select=cited_by_count"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "meiyi1986.github.io stats"}), timeout=20) as r:
                n = int(json.load(r)["cited_by_count"])
            raw[doi], out[doi] = n, plus(n)
            fetched += 1
        except Exception as e:  # keep the previous value
            print(f"  citations: could not fetch {doi}: {e}")
    return out, raw, fetched


def main():
    previous = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    stats = {"grantsawards": grants_awards(), "services": services(), "supervision": supervision(),
             "teaching": teaching(), "publications": publications()}
    stats["citations"], stats["citations_raw"], fetched = citations(previous)
    stats["citations_updated"] = (datetime.date.today().strftime("%B %Y") if fetched
                                  else previous.get("citations_updated", ""))
    OUT.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for k, v in stats.items():
        if k not in ("citations", "citations_raw"):
            print(k, v)
    print(f"citations: {fetched}/{len(stats['citations'])} fetched")


if __name__ == "__main__":
    main()
