#!/usr/bin/env python3
"""Generate the research theme pages (_pages/research-*.md) and the
Research Themes section of the homepage from the BibTeX files.

Run from the repository root:  python3 _scripts/research_pages.py
Edit the THEMES content below and re-run; hand edits to the generated
pages are overwritten.
"""
import collections
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg import svg, node, edge, box, arrow, text, region, bar_chart  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "_publications"
FILES = {"J": ("publication-journal.bib", "publication-journal.html"),
         "C": ("publication-conf.bib", "publication-conf.html"),
         "B": ("publication-book.bib", "publication-book.html"),
         "Ch": ("publication-chapter.bib", "publication-chapter.html")}
LAST_YEAR = 2026

# ---------------------------------------------------------------- BibTeX
RECS, ALL = {}, []
for kind, (bib, page) in FILES.items():
    for e in re.split(r"\n\s*@", (PUB / bib).read_text(encoding="utf-8")):
        if "{" not in e:
            continue
        key = e.split("{", 1)[1].split(",")[0].strip()

        def g(k, e=e):
            m = re.search(r"\b" + k + r"\s*=\s*\{(.*?)\}\s*,?\s*\n", e, re.S)
            return m.group(1).replace("\n", " ").strip() if m else ""
        r = dict(key=key, kind=kind, page=page, title=g("title"), year=g("year"),
                 venue=g("journal") or g("booktitle") or g("publisher"), doi=g("doi"))
        RECS[(kind, key)] = r
        ALL.append(r)
# these two entries share one DOI in the BibTeX; link to the list entry instead
for k in [("J", "sun2024cooperative"), ("J", "sun2024multi")]:
    if k in RECS:
        RECS[k]["doi"] = ""


def clean(s):
    return re.sub(r"[{}]", "", s).replace("\\alpha", "α").replace("--", "–")


def item(kind, key, badge=None, note=None):
    r = RECS[(kind, key)]
    href = f"https://doi.org/{r['doi']}" if r["doi"] else f"/publications/{r['page']}#{key}"
    venue = re.sub(r"^Proceedings of (the )?", "", clean(r["venue"]))
    b = f' <span class="badge badge--award">{badge}</span>' if badge else ""
    n = f' <span class="contrib-list__note">{note}</span>' if note else ""
    return (f'  <li><a class="contrib-list__title" href="{href}">{html.escape(clean(r["title"]))}</a>'
            f'<span class="contrib-list__venue"><i>{html.escape(venue)}</i>, {r["year"]} · '
            f'<a href="/publications/{r["page"]}#{key}">list entry</a></span>{b}{n}</li>')


def clist(*items):
    return '<ul class="contrib-list">\n' + "\n".join(items) + "\n</ul>"


def fig(s, cap):
    return f'<figure class="theme-figure">\n{s}\n<figcaption>{cap}</figcaption>\n</figure>'


def J(k, **kw): return item("J", k, **kw)
def C(k, **kw): return item("C", k, **kw)


def classify(pattern, exclude=None):
    out = [r for r in ALL if r["kind"] in ("J", "C", "B", "Ch") and re.search(pattern, r["title"], re.I)
           and not (exclude and re.search(exclude, r["title"], re.I))]
    cnt = collections.Counter((r["year"], "C" if r["kind"] == "C" else "J") for r in out)
    return out, cnt


# ---------------------------------------------------------------- figures
def fig_carp():
    pts = {"D": (360, 120), "a": (200, 50), "b": (110, 120), "c": (200, 200), "d": (520, 45),
           "e": (630, 110), "f": (560, 205), "g": (360, 30), "h": (380, 215)}
    base = [("D", "a"), ("a", "b"), ("b", "c"), ("c", "D"), ("D", "d"), ("d", "e"), ("e", "f"),
            ("f", "D"), ("D", "g"), ("g", "a"), ("g", "d"), ("D", "h"), ("h", "c"), ("h", "f")]
    routes = {1: [("a", "b"), ("b", "c")], 2: [("d", "e"), ("e", "f")], 3: [("g", "d"), ("h", "c")]}
    out = []
    for u, v in base:
        (x1, y1), (x2, y2) = pts[u], pts[v]
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="svg-road"/>')
    for rid, es in routes.items():
        for u, v in es:
            (x1, y1), (x2, y2) = pts[u], pts[v]
            out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="svg-route svg-route--{rid}"/>')
    for k, (x, y) in pts.items():
        if k == "D":
            out.append(f'<rect x="{x - 16}" y="{y - 16}" width="32" height="32" rx="4" class="svg-fn"/>'
                       + text(x, y + 5, "Depot", "svg-fn-text svg-small"))
        else:
            out.append(f'<circle cx="{x}" cy="{y}" r="7" class="svg-term"/>')
    legend = "".join(f'<line x1="{20 + i * 150}" y1="250" x2="{50 + i * 150}" y2="250" class="svg-route svg-route--{i + 1}"/>'
                     + text(58 + i * 150, 254, f"route of vehicle {i + 1}", "svg-axis", "start") for i in range(3))
    legend += f'<line x1="470" y1="250" x2="500" y2="250" class="svg-road"/>' + text(508, 254, "road (no service needed)", "svg-axis", "start")
    return svg(720, 265, "".join(out) + legend, "Capacitated arc routing example",
               "A depot and a road network; coloured streets must be served, and each colour is one vehicle's route.")


def fig_memetic():
    b = (box(20, 40, 170, 60, ["Population of", "candidate solutions"])
         + box(270, 40, 170, 60, ["Crossover", "(recombine routes)"])
         + box(520, 40, 180, 60, ["Local search", "e.g. Merge-Split operator"], "svg-box svg-box--accent")
         + box(270, 150, 170, 60, ["Selection &amp;", "replacement"])
         + arrow("M190,70 L266,70") + arrow("M440,70 L516,70")
         + arrow("M610,100 Q610,180 444,180") + arrow("M270,180 Q105,180 105,104"))
    return svg(720, 225, b, "Memetic algorithm",
               "Evolutionary search combined with problem-specific local search.")


def fig_cc():
    cols = [1, 2, 1, 3, 2, 3, 1, 2, 3, 1, 3, 2]
    out = [text(360, 18, "LARGE-SCALE PROBLEM: many interacting decision variables", "svg-region-title")]
    for i, c in enumerate(cols):
        x = 72 + i * 48
        out.append(f'<rect x="{x}" y="30" width="38" height="30" rx="4" class="svg-group svg-group--{c}"/>'
                   + text(x + 19, 50, f"x{i + 1}", "svg-small-dark"))
    out.append(text(360, 86, "① detect interactions (e.g. differential grouping) and group variables", "svg-axis"))
    for g in range(3):
        x = 60 + g * 220
        out.append(box(x, 100, 180, 50, [f"optimise group {g + 1}"], f"svg-box svg-group--{g + 1}"))
        out.append(arrow(f"M{x + 90},150 L{360 + (g - 1) * 40},186"))
    out.append(box(240, 190, 240, 44, ["② combine via shared context solution"], "svg-box svg-box--accent"))
    return svg(720, 245, "".join(out), "Cooperative co-evolution by decomposition",
               "Variables are grouped by interaction, each group is optimised separately, and results are combined.")


def fig_tree():
    b = (edge(170, 38, 90, 118) + edge(170, 38, 250, 118) + edge(250, 118, 200, 196) + edge(250, 118, 300, 196)
         + node(170, 38, "+", True) + node(90, 118, "PT", False) + node(250, 118, "÷", True)
         + node(200, 196, "WINQ", False) + node(300, 196, "NOR", False)
         + '<circle cx="6" cy="222" r="5" class="svg-fn"/>' + text(14, 226, "function", "svg-axis", "start")
         + '<circle cx="82" cy="222" r="5" class="svg-term"/>' + text(90, 226, "terminal (job / machine feature)", "svg-axis", "start"))
    return svg(340, 232, b, "A dispatching rule as a GP tree: PT + WINQ / NOR", cls="theme-svg theme-svg--narrow")


def fig_gphh():
    b = (region(6, 6, 476, 258, "OFFLINE · learn the heuristic")
         + region(506, 6, 248, 258, "ONLINE · use the heuristic", "svg-region svg-region--online")
         + box(24, 52, 196, 64, ["1. Population of", "candidate rules (GP trees)"])
         + box(266, 52, 196, 64, ["2. Evaluate each rule in", "simulated dynamic scenarios"])
         + box(145, 170, 196, 64, ["3. Select &amp; vary", "(crossover, mutation)"])
         + arrow("M220,84 L262,84") + arrow("M364,116 Q364,150 322,170") + arrow("M164,170 Q122,150 122,120")
         + box(526, 52, 208, 64, ["Best evolved rule", "(compact, interpretable)"], "svg-box svg-box--accent")
         + box(526, 170, 208, 64, ["Real-time decisions: rank", "waiting jobs / vehicles / tasks"])
         + arrow("M462,84 L522,84") + arrow("M630,116 L630,166"))
    return svg(760, 270, b, "GP hyper-heuristic workflow",
               "Offline, candidate rules are evolved in simulation; online, the best rule makes real-time decisions.")


def fig_timeline():
    out = [f'<line x1="40" y1="120" x2="690" y2="120" class="svg-edge"/>',
           arrow("M680,120 L700,120")]
    events = [(90, "job arrives"), (200, "machine idle → rule ranks queue"), (330, "machine breaks down"),
              (450, "urgent job arrives"), (580, "vehicle idle → rule picks next task")]
    for i, (x, lab) in enumerate(events):
        up = i % 2 == 0
        y = 70 if up else 170
        out.append(f'<circle cx="{x}" cy="120" r="8" class="{"svg-fn" if "rule" in lab else "svg-term"}"/>')
        out.append(f'<line x1="{x}" y1="{112 if up else 128}" x2="{x}" y2="{y + (10 if up else -14)}" class="svg-road"/>')
        out.append(text(x, y, lab, "svg-label"))
    out.append(text(700, 145, "time", "svg-axis", "end"))
    return svg(720, 200, "".join(out), "Real-time decision points",
               "Dynamic events arrive over time; at each decision point the evolved rule decides instantly.")


def fig_rep():
    b = (text(150, 20, "TREE-BASED GP", "svg-region-title")
         + edge(150, 52, 90, 122) + edge(150, 52, 210, 122) + edge(210, 122, 170, 190) + edge(210, 122, 250, 190)
         + node(150, 52, "+", True) + node(90, 122, "PT", False) + node(210, 122, "÷", True)
         + node(170, 190, "WINQ", False) + node(250, 190, "NOR", False)
         + text(350, 120, "≡", "svg-big") + text(545, 20, "LINEAR GP", "svg-region-title")
         + '<rect x="420" y="40" width="250" height="150" rx="8" class="svg-code"/>'
         + "".join(text(440, 78 + i * 30, l, "svg-code-text", "start")
                   for i, l in enumerate(["r1 ← WINQ ÷ NOR", "r0 ← PT + r1", "return r0"]))
         + text(545, 212, "registers let sub-results be reused (a graph, not a tree)", "svg-axis"))
    return svg(700, 220, b, "Tree-based and linear representations")


def fig_plugins():
    stages = [("Initialise", "learned initialisation", "heuristic"), ("Choose operator", "adaptive operator", "selection"),
              ("Search neighbourhood", "learned / neural", "neighbourhood search"), ("Accept &amp; update", "RL-guided", "policies")]
    out = [region(10, 10, 700, 92, "THE OPTIMISER'S LOOP")]
    for i, (s, a, b2) in enumerate(stages):
        x = 30 + i * 172
        out.append(box(x, 42, 150, 44, [s]))
        if i < 3:
            out.append(arrow(f"M{x + 150},64 L{x + 168},64"))
        out.append(arrow(f"M{x + 75},150 L{x + 75},90", "svg-arrow svg-arrow--gold"))
        out.append(box(x, 150, 150, 50, [a, b2], "svg-box svg-box--gold", "svg-label svg-small"))
    out.append(arrow("M650,86 Q700,120 650,42") if False else "")
    out.append(region(10, 216, 700, 46, None, "svg-region svg-region--online"))
    out.append(text(360, 244, "Automated algorithm design: generate the whole optimiser (GP, lifelong optimiser generation)", "svg-label"))
    return svg(720, 270, "".join(out), "Where machine learning plugs into an optimiser",
               "Learned components for initialisation, operator selection, neighbourhood search and acceptance.")


def fig_aos():
    b = (box(20, 70, 150, 60, ["Search state", "(features)"])
         + box(230, 70, 170, 60, ["Selector", "(learned from experience)"], "svg-box svg-box--accent")
         + "".join(box(470, 20 + i * 44, 110, 34, [f"operator {i + 1}"], "svg-box" + (" svg-box--gold" if i == 2 else ""))
                   for i in range(4))
         + box(620, 70, 90, 60, ["new", "solution"])
         + arrow("M170,100 L226,100") + arrow("M400,100 L466,110") + arrow("M580,110 L616,104")
         + arrow("M665,130 Q665,200 315,200 Q300,200 312,134")
         + text(480, 215, "reward = improvement → update selector", "svg-axis"))
    return svg(720, 225, b, "Adaptive operator selection",
               "A selector picks which operator to apply from the search state and learns from the reward.")


def fig_xai_paths():
    b = (region(10, 10, 340, 200, "POST-HOC EXPLANATION")
         + box(30, 56, 120, 56, ["black-box", "model"], "svg-box svg-box--dark", "svg-label svg-light")
         + arrow("M150,84 L196,84")
         + box(200, 46, 136, 34, ["feature importance"], "svg-box", "svg-label svg-small")
         + box(200, 92, 136, 34, ["counterfactuals"], "svg-box", "svg-label svg-small")
         + box(200, 138, 136, 34, ["local surrogates"], "svg-box", "svg-label svg-small")
         + text(90, 150, "explain decisions", "svg-axis") + text(90, 166, "after training", "svg-axis")
         + region(370, 10, 340, 200, "INTERPRETABLE BY DESIGN", "svg-region svg-region--online")
         + '<rect x="400" y="56" width="280" height="56" rx="8" class="svg-code"/>'
         + text(540, 90, "priority = PT + WINQ ÷ NOR", "svg-code-text")
         + text(540, 140, "the model itself is a readable formula,", "svg-label")
         + text(540, 160, "kept small and dimensionally consistent", "svg-label"))
    return svg(720, 220, b, "Two routes to explainable AI")


def fig_cf():
    out = ['<path d="M60,220 C200,200 260,40 680,30" class="svg-boundary"/>',
           text(600, 60, "decision boundary", "svg-axis"),
           text(140, 60, "outcome A", "svg-region-title"), text(560, 200, "outcome B", "svg-region-title")]
    x0, y0 = 250, 170
    out.append(f'<circle cx="{x0}" cy="{y0}" r="10" class="svg-fn"/>' + text(x0 - 4, y0 + 32, "original input x", "svg-label"))
    for (x, y) in [(390, 150), (330, 70), (470, 120)]:
        out.append(f'<line x1="{x0}" y1="{y0}" x2="{x}" y2="{y}" class="svg-dashed"/>'
                   f'<circle cx="{x}" cy="{y}" r="9" class="svg-cf"/>')
    out.append(text(470, 96, "diverse counterfactuals x′", "svg-label"))
    out.append(text(360, 240, "“If these features had been slightly different, the decision would change.”", "svg-axis"))
    return svg(720, 250, "".join(out), "Counterfactual explanations",
               "Several minimal changes to the input that each flip the model's decision.")


def fig_tradeoff():
    x0, x1, y0, y1 = 70, 680, 20, 200
    pts = [(0.05, 0.92), (0.1, 0.62), (0.18, 0.42), (0.3, 0.3), (0.45, 0.24), (0.65, 0.2), (0.9, 0.18)]
    dom = [(0.25, 0.7), (0.5, 0.5), (0.7, 0.42), (0.4, 0.65), (0.85, 0.35), (0.6, 0.6)]
    X = lambda v: x0 + (x1 - x0) * v
    Y = lambda v: y1 - (y1 - y0) * v
    out = [f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" class="svg-edge"/>',
           f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" class="svg-edge"/>',
           text((x0 + x1) / 2, y1 + 26, "rule size (complexity) →", "svg-axis"),
           f'<text x="24" y="{(y0 + y1) / 2}" transform="rotate(-90 24 {(y0 + y1) / 2})" text-anchor="middle" class="svg-axis">decision error →</text>']
    out.append('<polyline points="' + " ".join(f"{X(a):.0f},{Y(b):.0f}" for a, b in pts) + '" class="svg-front"/>')
    out += [f'<circle cx="{X(a):.0f}" cy="{Y(b):.0f}" r="5" class="svg-term"/>' for a, b in dom]
    out += [f'<circle cx="{X(a):.0f}" cy="{Y(b):.0f}" r="6" class="svg-fn"/>' for a, b in pts]
    kx, ky = X(0.18), Y(0.42)
    out.append(f'<circle cx="{kx:.0f}" cy="{ky:.0f}" r="13" class="svg-knee"/>' + text(kx + 20, ky + 26, "small and accurate", "svg-label", "start"))
    out.append(text(X(0.72), Y(0.1), "trade-off front of evolved rules", "svg-label"))
    return svg(720, 240, "".join(out), "Interpretability–performance trade-off (schematic)")


def fig_paradigms():
    out = [region(6, 6, 228, 190, "TRANSFER"), region(246, 6, 228, 190, "MULTITASK"),
           region(486, 6, 228, 190, "LIFELONG", "svg-region svg-region--online")]
    out += [box(26, 60, 80, 44, ["source"]), box(134, 60, 80, 44, ["target"], "svg-box svg-box--accent"),
            arrow("M106,82 L130,82"), text(120, 140, "learn once, reuse", "svg-axis"), text(120, 156, "on a new task", "svg-axis")]
    out += [box(266, 60, 80, 44, ["task A"], "svg-box svg-box--accent"), box(374, 60, 80, 44, ["task B"], "svg-box svg-box--accent"),
            arrow("M346,74 L370,74"), arrow("M374,92 L350,92"), text(360, 140, "learn related tasks", "svg-axis"), text(360, 156, "together, sharing knowledge", "svg-axis")]
    for i in range(3):
        x = 500 + i * 70
        out.append(box(x, 52, 58, 36, [f"T{i + 1}"], "svg-box svg-box--accent"))
        if i < 2:
            out.append(arrow(f"M{x + 58},70 L{x + 68},70"))
        out.append(arrow(f"M{x + 29},88 L{x + 29},118", "svg-arrow svg-arrow--gold"))
    out.append(box(500, 120, 198, 30, ["growing knowledge base"], "svg-box svg-box--gold", "svg-label svg-small"))
    out.append(text(600, 176, "keep learning without forgetting", "svg-axis"))
    return svg(720, 205, "".join(out), "Transfer, multitask and lifelong learning")


def fig_multitask():
    b = (box(20, 30, 230, 120, [""], "svg-region") + text(135, 56, "TASK A", "svg-region-title") + text(135, 76, "e.g. minimise mean flowtime", "svg-axis")
         + box(450, 30, 230, 120, [""], "svg-region") + text(565, 56, "TASK B", "svg-region-title") + text(565, 76, "e.g. minimise mean tardiness", "svg-axis")
         + "".join(f'<circle cx="{x}" cy="{y}" r="9" class="svg-term"/>' for x, y in [(70, 110), (105, 124), (140, 104), (175, 122), (500 + 35 * 1, 124), (570, 104), (605, 122), (640, 108)])
         + '<circle cx="210" cy="108" r="9" class="svg-fn"/><circle cx="500" cy="110" r="9" class="svg-fn"/>'
         + arrow("M262,78 C320,40 380,40 440,78") + arrow("M440,112 C380,150 320,150 262,112")
         + text(350, 40, "transfer promising individuals") + text(350, 166, "share building blocks")
         + box(250, 176, 200, 30, ["surrogates rank rules cheaply"], "svg-box svg-box--accent"))
    return svg(700, 210, b, "Multitask GP with knowledge transfer")


def fig_lifelong():
    out = [text(360, 20, "A STREAM OF OPTIMISATION TASKS ARRIVES OVER TIME", "svg-region-title")]
    for i, t in enumerate(["CVRP", "VRP + time windows", "VRP + pickup", "new variant …"]):
        x = 30 + i * 172
        out.append(box(x, 34, 150, 40, [t], "svg-box"))
        if i < 3:
            out.append(arrow(f"M{x + 150},54 L{x + 168},54"))
    out += [box(250, 110, 220, 56, ["Learner", "(neural solver / optimiser generator)"], "svg-box svg-box--accent"),
            arrow("M360,76 L360,106"),
            box(520, 110, 180, 56, ["memory of past", "behaviour"], "svg-box svg-box--gold"),
            arrow("M520,138 L474,138", "svg-arrow svg-arrow--gold"),
            text(600, 186, "consolidate, don’t forget", "svg-axis"),
            box(20, 110, 180, 56, ["good on new", "and old tasks"], "svg-box"),
            arrow("M250,138 L204,138")]
    return svg(720, 200, "".join(out), "Lifelong learning for optimisation")


# homepage thumbnails (160 x 110)
def mini_carp():
    p = [(80, 55), (30, 20), (25, 85), (135, 20), (140, 88), (80, 100), (80, 12)]
    out = "".join(f'<line x1="{p[0][0]}" y1="{p[0][1]}" x2="{x}" y2="{y}" class="svg-road"/>' for x, y in p[1:])
    out += (f'<polyline points="80,55 30,20 25,85 80,55" class="svg-route svg-route--1" fill="none"/>'
            f'<polyline points="80,55 135,20 140,88 80,55" class="svg-route svg-route--2" fill="none"/>'
            f'<polyline points="80,55 80,12" class="svg-route svg-route--3" fill="none"/>')
    out += "".join(f'<circle cx="{x}" cy="{y}" r="4" class="svg-term"/>' for x, y in p[1:])
    out += '<rect x="72" y="47" width="16" height="16" rx="3" class="svg-fn"/>'
    return svg(160, 110, out, "Vehicle routes from a depot", cls="theme-svg theme-card__svg")


def mini_tree():
    b = (edge(80, 22, 40, 62) + edge(80, 22, 120, 62) + edge(120, 62, 98, 96) + edge(120, 62, 142, 96)
         + node(80, 22, "+", True, 14) + node(40, 62, "PT", False, 14) + node(120, 62, "÷", True, 14)
         + node(98, 96, "W", False, 12) + node(142, 96, "N", False, 12))
    return svg(160, 110, b, "A GP rule tree", cls="theme-svg theme-card__svg")


def mini_plugins():
    b = (box(20, 14, 120, 34, ["optimiser"], "svg-box svg-box--accent")
         + "".join(box(8 + i * 50, 70, 44, 28, ["ML"], "svg-box svg-box--gold", "svg-label svg-small")
                   + arrow(f"M{30 + i * 50},70 L{40 + i * 25},50", "svg-arrow svg-arrow--gold") for i in range(3)))
    return svg(160, 110, b, "Learned components in an optimiser", cls="theme-svg theme-card__svg")


def mini_front():
    pts = [(20, 20), (32, 50), (52, 68), (80, 80), (115, 86), (145, 89)]
    b = ('<line x1="12" y1="98" x2="152" y2="98" class="svg-edge"/><line x1="12" y1="8" x2="12" y2="98" class="svg-edge"/>'
         + '<polyline points="' + " ".join(f"{x},{y}" for x, y in pts) + '" class="svg-front"/>'
         + "".join(f'<circle cx="{x}" cy="{y}" r="4" class="svg-fn"/>' for x, y in pts)
         + '<circle cx="52" cy="68" r="9" class="svg-knee"/>')
    return svg(160, 110, b, "Interpretability trade-off", cls="theme-svg theme-card__svg")


def mini_transfer():
    b = (box(10, 40, 40, 30, ["A"], "svg-box svg-box--accent") + box(110, 40, 40, 30, ["C"], "svg-box svg-box--accent")
         + box(60, 8, 40, 30, ["B"], "svg-box svg-box--accent")
         + arrow("M50,48 L60,32") + arrow("M100,32 L110,48") + arrow("M50,62 L106,62")
         + box(20, 82, 120, 22, ["shared knowledge"], "svg-box svg-box--gold", "svg-label svg-small"))
    return svg(160, 110, b, "Knowledge shared across tasks", cls="theme-svg theme-card__svg")


# ---------------------------------------------------------------- themes
THEMES = []


def theme(**kw):
    THEMES.append(kw)


theme(
    slug="evolutionary-combinatorial-optimisation", file="research-ec.md",
    title="Evolutionary Computation for Combinatorial Optimisation",
    short="Evolutionary Computation for Combinatorial Optimisation",
    icon="fa-route", mini=mini_carp,
    pattern=r"memetic|ant colony|swarm|evolutionary|co-?evolution|genetic algorithm|tabu|local search|neighbou?rhood search|decomposition|grouping|meta-?heuristic|NSGA|divide-and-conquer|repair operator|knee",
    exclude=r"genetic programming|neural architecture|counterfactual|feature selection|text classif|machine learning|SHAP|intrusion",
    card_intro="Designing evolutionary and memetic algorithms that find high-quality solutions to hard routing, scheduling and allocation problems — and scaling them to very large instances by decomposition.",
    card_contrib="MAENS and decomposition-based memetic algorithms for arc routing; differential grouping and cooperative co-evolution for large-scale optimisation (IEEE TEVC Outstanding Paper Award).",
    lead="Many of society's logistics problems — collecting waste, gritting roads, delivering parcels, allocating cloud resources — are <b>combinatorial optimisation</b> problems: the number of possible solutions explodes with problem size. I design <b>evolutionary and memetic algorithms</b> that find near-optimal solutions quickly, and <b>decomposition</b> methods that let them scale to problems with thousands of decisions.",
    stats=[('{{ site.data.stats.citations["10.1109/tevc.2013.2281543"] }}', "citations of differential grouping (OpenAlex)"), ("TEVC", "Outstanding Paper Award 2017"),
           ("Runner-up", "Best Paper, IEEE ICWS 2018")],
    intro=lambda: f"""
<h3>The problems</h3>
<p>In the <b>capacitated arc routing problem (CARP)</b>, a fleet of vehicles with limited capacity must serve a set of streets — for example to collect waste — at minimum total cost. Related problems include vehicle routing with electric vehicles or drones, team orienteering, job shop scheduling and service allocation. They are NP-hard, so exact methods quickly become impractical.</p>
{fig(fig_carp(), '<b>Figure 1.</b> A small arc routing instance. Coloured streets require service; each colour is the route of one vehicle leaving and returning to the depot. Real instances have thousands of streets.')}
<h3>Why evolutionary computation?</h3>
<p>Evolutionary algorithms search with a <i>population</i> of solutions, recombining good ones. <b>Memetic algorithms</b> add problem-specific local search, combining global exploration with powerful local refinement. They handle complex constraints and multiple objectives naturally and give good solutions within practical time.</p>
{fig(fig_memetic(), '<b>Figure 2.</b> A memetic algorithm. Crossover explores new combinations of routes; local search, such as the large-step Merge-Split operator in MAENS, refines each offspring.')}
""",
    sections=lambda: [
        ("Memetic algorithms for arc routing",
         "We proposed MAENS, whose Merge-Split operator explores far beyond traditional local moves and became a widely used benchmark, and extended memetic search to multi-objective, periodic and uncertain arc routing.",
         clist(J("tang2009memetic"), J("mei2009global"), J("mei2011decomposition"), J("mei2011memetic"),
               J("zhang2017memetic"), C("mei2010capacitated"))),
        ("Large-scale optimisation by decomposition",
         f"""<p>Very large problems are solved by splitting them into smaller interacting sub-problems. Our <b>differential grouping</b> detects variable interactions automatically, and <b>route distance grouping</b> and route clustering decompose large arc routing problems.</p>
{fig(fig_cc(), '<b>Figure 3.</b> Cooperative co-evolution. Variables are grouped by their interactions; each group is optimised separately and the pieces are combined through a shared context solution.')}""",
         clist(J("omidvar2014cooperative", badge="TEVC Outstanding Paper Award"), J("omidvar2017dg2"),
               J("mei2016competitive"), J("mei2014cooperative"), J("zhang2020route"), J("zhang2023rocash2"),
               J("jia2020contribution"))),
        ("Vehicle routing and emerging logistics",
         "We design evolutionary algorithms for new logistics settings such as electric vehicles with charging, collaborative truck–drone delivery, multi-depot routing and orienteering.",
         clist(J("jia2021bi"), J("jia2022confidence"), J("zhai2024collaborative"), J("zhai2026collaborative"),
               J("zhai2026coevolution"), J("zhang2026effective"), J("mei2016efficient"))),
        ("Multi-objective and real-world optimisation",
         "Real decisions involve trade-offs. We develop multi-objective evolutionary algorithms for web services and cloud, air traffic flow management, airport ground movement, project scheduling and water networks.",
         clist(J("tan2018evolutionary"), C("da2018hybrid", badge="Best Paper Runner-Up, ICWS 2018"),
               J("guo2023knee"), J("guo2023cooperative"), J("yang2026qlearning"), J("tian2021multi"), J("jia2021two"))),
    ])

theme(
    slug="genetic-programming", file="research-gp.md",
    title="Genetic Programming for Real-time Optimisation and Decision-Making",
    short="Genetic Programming for Real-time Optimisation and Decision-Making",
    icon="fa-bolt", mini=mini_tree,
    pattern=r"genetic programming|hyper-?heuristic|dispatching rule|scheduling heuristic|routing polic|scheduling rule",
    exclude=None,
    card_intro="Evolving compact, interpretable decision rules with genetic programming that react instantly to dynamic events in factories, vehicle fleets, cloud data centres and traffic networks.",
    card_contrib="GP hyper-heuristics for dynamic scheduling and routing; the first book on the topic; EuroGP and GECCO Best Paper Awards; HUMIES Silver Award.",
    lead="Real-world systems change constantly: jobs arrive, machines break down, demands and travel times are uncertain. Re-optimising after every change is too slow. My research uses <b>genetic programming (GP)</b> to automatically learn <b>decision rules</b> that make high-quality decisions <b>in real time</b> — in microseconds, with formulas people can read.",
    stats=[("3", "EuroGP &amp; GECCO Best Paper Awards"), ("1st", "book on hyper-heuristics for production scheduling"),
           ("Humies", "Silver Award 2023")],
    intro=lambda: f"""
<h3>Decisions that cannot wait</h3>
<p>In a dynamic job shop, every time a machine becomes idle it must choose which waiting job to process next; in uncertain arc routing, a vehicle must choose its next street when it finishes a task. These decisions must be made immediately, using only the current state.</p>
{fig(fig_timeline(), '<b>Figure 1.</b> Dynamic events arrive over time. At each decision point (filled circles) an evolved rule ranks the options instantly.')}
<div class="theme-split">
{fig(fig_tree(), '<b>Figure 2.</b> A scheduling rule as a GP tree, computing priority <code>PT + WINQ / NOR</code> from processing time, work in the next queue and number of operations remaining.')}
<div class="theme-split__text">
<h3>Why genetic programming?</h3>
<ul>
<li><b>Learns the rule itself</b> — GP searches over programs, discovering new rule structures rather than tuning parameters.</li>
<li><b>Fast at decision time</b> — evaluating a formula takes microseconds.</li>
<li><b>Readable</b> — experts can inspect and trust the evolved rule.</li>
<li><b>Trained in simulation</b> — learned offline on many scenarios, reused online.</li>
</ul>
</div>
</div>
{fig(fig_gphh(), '<b>Figure 3.</b> A GP hyper-heuristic learns the rule offline in simulation; after a number of generations the best rule is deployed online.')}
""",
    sections=lambda: [
        ("Scheduling heuristics for dynamic job shops",
         "Our core line of work makes GP hyper-heuristics effective for dynamic (flexible) job shop scheduling: evolving routing and sequencing rules together, selecting the most useful features, and combining rules into ensembles. It is summarised in our Springer book and surveys.",
         clist(item("B", "zhang2021", note="Book"), J("nguyen2017genetic", note="Survey"), J("mei2017efficient"),
               J("zhang2020evolving"), J("xu2020genetic"), J("zhang2021correlation"), J("xu2023genetic2"),
               J("xu2023genetic"), J("zhang2023survey", note="Survey"))),
        ("Routing policies under uncertainty",
         "For arc and vehicle routing with uncertain demands and costs, we evolve routing policies that let each vehicle decide its next task on the fly, including vehicle collaboration, niching and multi-objective trade-offs.",
         clist(C("mei2018genetic1"), J("maclachlan2019genetic"), J("liu2019predictive"), J("wang2021genetic"),
               J("wang2022multi"))),
        ("New program representations",
         f"""<p>We introduced linear and grammar-guided linear GP to scheduling, enabling rules with reusable sub-expressions and flow-control logic.</p>
{fig(fig_rep(), '<b>Figure 4.</b> The same rule in tree-based GP and in linear GP, where registers store intermediate results for reuse.')}""",
         clist(C("huang2022investigation", badge="Best Paper Award, EuroGP 2022"),
               C("huang2023grammar", badge="Best Paper Award, GECCO 2023"),
               J("huang2023bridging"), J("huang2024toward"), J("huang2025cross"))),
        ("Learning faster with surrogates",
         "Evaluating a rule needs many simulations. Our surrogate models and multi-fidelity evaluation estimate rule quality cheaply, cutting training time substantially.",
         clist(C("zhang2018surrogate"), J("zhang2021collaborative"), J("zhang2022instance"), C("chen2024neural"),
               J("guo2024genetic"))),
        ("Real-time decisions beyond the factory",
         """<p>The same approach powers real-time decisions in many domains.</p>
<div class="theme-apps"><span class="badge">Traffic signal control</span><span class="badge">Cloud &amp; fog workflow scheduling</span><span class="badge">Air traffic flow management</span><span class="badge">Yard crane scheduling</span><span class="badge">Emergency medical dispatch</span><span class="badge">Multi-agent path planning</span></div>""",
         clist(C("liao2024learning", badge="Best Paper Award, GECCO 2024"), J("liao2025gplight+"),
               C("maclachlan2023learning", badge="HUMIES Silver Award 2023"), J("xu2023genetic1"),
               J("sun2024cooperative"), J("guo2026multitree"), J("jin2026semantic"), J("liao2024learning"))),
    ],
    see_also="Multitask learning, explainability and links with reinforcement learning in GP are covered under the other themes below.")

theme(
    slug="machine-learning-optimisation", file="research-ml-opt.md",
    title="Machine Learning and Automated Algorithm Design for Optimisation",
    short="Machine Learning and Automated Algorithm Design for Optimisation",
    icon="fa-cogs", mini=mini_plugins,
    pattern=r"learn|neural|reinforcement|operator selection|hyper-?heuristic|automated (heuristic |algorithm )?design|optimizer generation|sparsification|attention|MCTS|initialisation heuristic|penalisation criterion|guided local search|surrogate",
    exclude=r"counterfactual|explain|text classif|medical|essay|ontology|asset|bond|genomic|wind environment",
    card_intro="Using machine learning to make optimisers smarter — learning which operator to apply, where to search, and even how to design the algorithm itself.",
    card_contrib="Adaptive operator selection; learned and neural neighbourhood search for routing; GP-designed algorithm components; IEEE CIM Outstanding Paper Award; EvoStar 2026 Best Student Paper.",
    lead="Designing a good optimisation algorithm usually takes experts years of trial and error, and the result rarely transfers to new problems. My research uses <b>machine learning</b> to automate this: learning <b>which search operator to apply</b>, <b>where to search</b>, <b>how to start</b>, and ultimately <b>generating whole algorithms</b> automatically.",
    stats=[("TPAMI", "learning-aided neighbourhood search, 2025"), ("CIM", "Outstanding Paper Award 2026"),
           ("EvoStar", "Best Student Paper Award 2026")],
    intro=lambda: f"""
<h3>Learning inside the optimiser</h3>
<p>Every metaheuristic is built from components — how to initialise, which operator to apply, which neighbourhood to search, when to accept a move. Each is a decision that machine learning can make better than a fixed hand-designed choice, by learning from experience on many problem instances.</p>
{fig(fig_plugins(), '<b>Figure 1.</b> Where learning plugs into an optimiser. Learned components (gold) replace hand-designed choices; at the highest level, automated algorithm design generates the whole optimiser.')}
<h3>Two complementary learners</h3>
<p><b>Deep and reinforcement learning</b> learn flexible policies from data, while <b>genetic programming</b> learns compact, interpretable components. We study both and how they combine.</p>
""",
    sections=lambda: [
        ("Adaptive operator selection",
         f"""<p>Which operator works best changes during the search and across instances. We learn operator selectors from both offline and online experience, and surveyed the field.</p>
{fig(fig_aos(), '<b>Figure 2.</b> Adaptive operator selection: a selector chooses the next operator from features of the search state and is updated by the improvement it produces.')}""",
         clist(C("pei2024learning", badge="Best Paper Nomination, GECCO 2024"), C("pei2023local"),
               C("pei2022investigation"), J("pei2025adaptive", note="Survey"), J("consoli2016dynamic"))),
        ("Learning-guided and neural search for routing",
         "We combine neural networks with neighbourhood search and design neural solvers that generalise better across problem sizes and variants.",
         clist(J("guo2025learning"), J("guo2025emergency"), C("chen2025learning"), C("chen2026mode"),
               J("jia2025neural"), J("wang2025distance"), C("lin2026machine"))),
        ("Automated design of algorithm components",
         "GP and learning can design the components of other algorithms: initialisation heuristics, guided local search penalties, and ant colony state transition rules.",
         clist(C("costa2023learning"), C("costa2021learning2"), C("liu2024gpgls"),
               C("liu2026adaptive", badge="Best Student Paper Award, EvoStar 2026"), J("lin2025automated"),
               J("nguyen2019hybrid"))),
        ("Combining evolutionary computation and reinforcement learning",
         "We compare and hybridise GP and deep reinforcement learning for sequential decisions, and embed reinforcement learning inside evolutionary search.",
         clist(J("xu2023genetic3", badge="Outstanding Paper Award, IEEE CIM 2026"), J("xu2024learn", note="Survey"),
               J("xu2024niching"), J("yang2025dynamic"), J("jia2026self"), C("chen2026dyro"))),
    ])

theme(
    slug="explainable-ai", file="research-xai.md",
    title="Explainable AI",
    short="Explainable AI",
    icon="fa-search", mini=mini_front,
    pattern=r"explain|explanation|interpretab|counterfactual|(?-i:\bSHAP\b)|simplif|dimensionally aware|structural complexit",
    exclude=None,
    card_intro="Making AI decisions understandable — by evolving models that are interpretable by design, and by explaining the decisions of black-box models.",
    card_contrib="Survey on explainable AI by GP; local and counterfactual explanations for evolved policies; interpretability-aware GP; GECCO 2022 Best Paper Award; ITNAC 2025 Best Student Paper.",
    lead="AI is increasingly trusted with consequential decisions, from scheduling hospital resources to detecting cyber attacks. People need to <b>understand</b> and <b>trust</b> those decisions. My research makes AI explainable in two ways: building models that are <b>interpretable by design</b>, and <b>explaining</b> the decisions of complex models after training.",
    stats=[('{{ site.data.stats.citations["10.1109/tevc.2022.3225509"] }}', "citations of our XAI-by-GP survey (OpenAlex)"), ("GECCO", "Best Paper Award 2022"),
           ("ITNAC", "Best Student Paper Award 2025")],
    intro=lambda: f"""
<h3>Two routes to explainability</h3>
<p>A black-box model, such as a deep neural network, can be explained <i>post hoc</i> — which features mattered, or what would have to change to get a different outcome. Alternatively, the model can be <i>interpretable by design</i>: a short formula evolved by genetic programming can be read directly.</p>
{fig(fig_xai_paths(), '<b>Figure 1.</b> Post-hoc explanation versus interpretable-by-design models. Our work spans both.')}
""",
    sections=lambda: [
        ("Genetic programming for explainable AI",
         "We surveyed how GP contributes to explainable AI, both by evolving interpretable models and by producing explanations for black-box models, and use GP to build interpretable local explanations.",
         clist(J("mei2022explainable", note="Survey"), C("andersen2024interpretable"))),
        ("Explaining evolved decision policies",
         "Even evolved rules can grow large. We explain them by ranking the features that drive each decision and by generating counterfactual what-if scenarios.",
         clist(C("wang2022local", badge="Best Paper Award, GECCO 2022"), J("wang2023explaining"),
               C("wang2024preliminary"), C("wang2025diverse"))),
        ("Counterfactual explanations",
         f"""<p>A counterfactual tells a user the smallest change that would alter a decision. We evolve sets of <b>diverse</b> counterfactuals so users see several plausible alternatives.</p>
{fig(fig_cf(), '<b>Figure 2.</b> Diverse counterfactual explanations: several minimal changes to the input, each of which crosses the decision boundary.')}""",
         clist(C("andersen2022evolving"), C("andersen2023producing"))),
        ("Interpretable-by-design heuristics",
         f"""<p>We keep evolved rules small, simple and physically meaningful by enforcing dimensional consistency, simplifying expressions, and optimising interpretability as an explicit objective.</p>
{fig(fig_tradeoff(), '<b>Figure 3.</b> Schematic interpretability–performance trade-off. Multi-objective GP finds a front of rules; rules near the knee are both small and accurate.')}""",
         clist(C("mei2017constrained"), C("panda2022simplifying"), C("zhang2023interpretability"),
               C("pang2024multi"), J("pang2026balancing"), J("zhang2026genetic"))),
        ("Explainable machine learning in applications",
         "We make machine learning explainable in security and healthcare, for example robust SHAP explanations for intrusion detection.",
         clist(C("hendro2025investigation", badge="Best Student Paper Award, ITNAC 2025"), C("hendro2026enhancing"),
               C("abdollahi2018uncovering"))),
    ])

theme(
    slug="transfer-multitask-lifelong-learning", file="research-transfer.md",
    title="Transfer, Multitask, and Lifelong Machine Learning",
    short="Transfer, Multitask, and Lifelong Machine Learning",
    icon="fa-project-diagram", mini=mini_transfer,
    pattern=r"transfer|multi-?task|multitasking|lifelong|reusab|generali[sz]|cross-problem|curriculum|offline and online experiences|parameter sharing",
    exclude=r"transfer function|Multi-Task Fuzzy",
    card_intro="Reusing knowledge across related problems so that learning is faster and generalises better — from one task to another, across tasks at once, and over a lifetime of tasks.",
    card_contrib="Knowledge-transfer and multitask GP; lifelong learning for optimiser generation and neural routing solvers (IJCAI 2025, ICLR 2026); EuroGP 2022 Best Paper Award.",
    lead="Problems rarely come alone. A factory faces many related scheduling scenarios; a logistics company solves new variants of routing every day. Instead of learning each from scratch, my research <b>reuses knowledge</b> — through <b>transfer</b> learning, <b>multitask</b> learning and <b>lifelong</b> learning — so that solvers learn faster and generalise further.",
    stats=[("ICLR", "2026 — lifelong learning for routing"), ("IJCAI", "2025 — lifelong optimiser generation"),
           ("EuroGP", "Best Paper Award 2022")],
    intro=lambda: f"""
<h3>Three ways to reuse knowledge</h3>
<p><b>Transfer learning</b> reuses what was learned on a source task to speed up a target task. <b>Multitask learning</b> solves several related tasks together so they help each other. <b>Lifelong learning</b> faces a stream of tasks and must keep improving without forgetting earlier ones.</p>
{fig(fig_paradigms(), '<b>Figure 1.</b> Transfer, multitask and lifelong learning.')}
""",
    sections=lambda: [
        ("Knowledge transfer in genetic programming",
         "We transfer useful sub-trees, individuals and search distributions between GP runs on related routing problems, and studied how reusable evolved rules are.",
         clist(item("Ch", "mei2021knowledge", note="Book chapter"), C("mei2016comprehensive"), C("ardeh2019genetic"),
               C("ardeh2020parametric"), J("ardeh2021genetic"), J("ardeh2022knowledge"))),
        ("Evolutionary multitask learning",
         f"""<p>Multitask GP learns heuristics for several scenarios simultaneously, deciding which tasks are related and what to share.</p>
{fig(fig_multitask(), '<b>Figure 2.</b> Multitask GP shares promising individuals and building blocks between tasks, and uses surrogates to save evaluations.')}""",
         clist(C("park2018evolutionary"), C("zhang2020evolutionary"), J("zhang2020surrogate"), J("zhang2021multitask"),
               J("zhang2022task"), J("zhang2022multitask"), C("huang2022investigation", badge="Best Paper Award, EuroGP 2022"),
               J("huang2023multitask"), C("ardeh2021novel"))),
        ("Lifelong learning for optimisation",
         f"""<p>When new problem variants keep arriving, a learner must adapt without forgetting. We consolidate past behaviour to keep performance on earlier tasks while learning new ones.</p>
{fig(fig_lifelong(), '<b>Figure 3.</b> Lifelong learning for optimisation: a learner faces a stream of routing variants and consolidates its past behaviour to avoid forgetting.')}""",
         clist(C("pei2026lifelong", note="ICLR 2026"), C("pei2025libog", note="IJCAI 2025"), C("pei2024learning"))),
        ("Generalising across problems",
         "We improve how learned solvers and heuristics generalise to new sizes, variants and objectives, with parameter sharing, attention reshaping and curriculum learning.",
         clist(J("wang2025soft"), J("wang2025distance"), C("liu2025curriculum"), C("qiao2026enhancing"),
               C("hardwick2017evolving"))),
    ])


# ---------------------------------------------------------------- render
def stat(v, l):
    return f'  <div class="home-stat"><span class="home-stat__value">{v}</span><span class="home-stat__label">{l}</span></div>'


def theme_nav(current):
    links = []
    for t in THEMES:
        attr = ' class="is-current" aria-current="page"' if t["slug"] == current else ""
        links.append(f'  <a href="/research/{t["slug"]}/"{attr}><i class="fas {t["icon"]}" aria-hidden="true"></i> {t["short"]}</a>')
    return '<nav class="pub-jump theme-others" aria-label="Research themes">\n' + "\n".join(links) + "\n</nav>"


def render(t):
    papers, cnt = classify(t["pattern"], t["exclude"])
    years = [str(y) for y in range(min(int(r["year"]) for r in papers), LAST_YEAR + 1)]
    n = len(papers)
    nlabel = f"{(n // 10) * 10}+" if n >= 20 else str(n)
    stats = [stat(nlabel, "papers in this theme")] + [stat(v, l) for v, l in t["stats"]]
    secs = []
    for i, (name, body, lst) in enumerate(t["sections"](), 1):
        body = body if body.lstrip().startswith("<") else f"<p>{body}</p>"
        secs.append(f'<h3 class="theme-sub"><span class="theme-sub__num">{i}</span> {name}</h3>\n{body}\n{lst}')
    see = f'<p class="contrib-list__extra">{t["see_also"]}</p>\n' if t.get("see_also") else ""
    nfig = len(re.findall(r"<b>Figure \d+\.", t["intro"]() + "".join(s[1] for s in t["sections"]())))
    chart = fig(bar_chart(cnt, years),
                f'<b>Figure {nfig + 1}.</b> My papers in this theme per year ({n} in total), identified by title keywords in my '
                f'<a href="/publications/">publication lists</a>; papers can belong to more than one theme. The {LAST_YEAR} count covers papers published so far this year.')
    excerpt = re.sub(r"<[^>]+>", "", t["lead"])[:300].replace('"', "'")
    return f"""---
layout: archive
title: "{t['title']}"
permalink: /research/{t['slug']}/
excerpt: "{excerpt}"
author_profile: true
---
<!-- Generated by _scripts/research_pages.py; edit that script and re-run instead of editing this file. -->

<p class="theme-lead">{t['lead']}</p>

<section class="home-stats page-highlights" aria-label="Highlights">
{chr(10).join(stats)}
</section>

<nav class="pub-jump" aria-label="On this page">
  <a href="#introduction"><i class="fas fa-lightbulb" aria-hidden="true"></i> Introduction</a>
  <a href="#contributions"><i class="fas fa-star" aria-hidden="true"></i> Contributions</a>
  <a href="#output"><i class="fas fa-chart-bar" aria-hidden="true"></i> Research output</a>
</nav>

<a name="introduction"></a>
<h2>Introduction</h2>
{t['intro']().strip()}

<a name="contributions"></a>
<h2>My Contributions</h2>
<p>With my students and collaborators, I have made the following contributions. Click a title to read the paper, or <i>list entry</i> to see it in my publication list.</p>

{chr(10).join(secs)}

{see}<a name="output"></a>
<h2>Research Output</h2>
{chart}

<h2>Research Themes</h2>
{theme_nav(t['slug'])}

<p class="home-more"><a href="/publications/">Full publication list →</a> &nbsp; <a href="/">← Back to home</a></p>
"""


def homepage_section():
    cards = []
    for t in THEMES:
        papers, _ = classify(t["pattern"], t["exclude"])
        url = f"/research/{t['slug']}/"
        cards.append(f"""  <article class="theme-card">
    <a class="theme-card__demo" href="{url}" aria-hidden="true" tabindex="-1">{t['mini']()}</a>
    <div class="theme-card__body">
      <h3><a href="{url}"><i class="fas {t['icon']}" aria-hidden="true"></i> {t['short']}</a></h3>
      <p>{t['card_intro']}</p>
      <p class="theme-card__contrib"><b>Contributions:</b> {t['card_contrib']}</p>
      <a class="home-theme__more" href="{url}">{len(papers)} papers · Explore this theme →</a>
    </div>
  </article>""")
    return ("<!-- ===================== RESEARCH THEMES ===================== -->\n"
            "<!-- Generated by _scripts/research_pages.py -->\n"
            '<a name="research-interests"></a>\n<h2 class="home-section-title">Research Themes</h2>\n'
            '<div class="theme-cards">\n' + "\n".join(cards) + "\n</div>\n\n")


def main():
    for t in THEMES:
        (ROOT / "_pages" / t["file"]).write_text(render(t), encoding="utf-8")
        print("wrote", t["file"])
    about = ROOT / "_pages" / "about.md"
    s = about.read_text(encoding="utf-8")
    a = s.index("<!-- ===================== RESEARCH THEMES ===================== -->")
    b = s.index("<!-- ===================== NEWS ===================== -->")
    about.write_text(s[:a] + homepage_section() + s[b:], encoding="utf-8")
    print("updated about.md")


if __name__ == "__main__":
    main()
