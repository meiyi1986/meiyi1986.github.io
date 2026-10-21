"""Small SVG helpers for the research theme pages (styled by .theme-svg in main.scss)."""

DEFS = ('<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
        'class="svg-arrowhead"/></marker></defs>')


def svg(w, h, body, title, desc="", cls="theme-svg"):
    d = f"<desc>{desc}</desc>" if desc else ""
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{d}{DEFS}{body}</svg>")


def node(x, y, label, fn, r=21):
    c = "svg-fn" if fn else "svg-term"
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="{c}"/>'
            f'<text x="{x}" y="{y + 5}" text-anchor="middle" class="{c}-text">{label}</text>')


def edge(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="svg-edge"/>'


def box(x, y, w, h, lines, cls="svg-box", tcls="svg-label"):
    t = "".join(f'<tspan x="{x + w / 2}" dy="{0 if i == 0 else 17}">{l}</tspan>'
                for i, l in enumerate(lines))
    ty = y + h / 2 - (len(lines) - 1) * 8.5 + 5
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>'
            f'<text y="{ty}" text-anchor="middle" class="{tcls}">{t}</text>')


def arrow(d, cls="svg-arrow"):
    return f'<path d="{d}" class="{cls}" marker-end="url(#arr)"/>'


def text(x, y, s, cls="svg-label", anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{s}</text>'


def region(x, y, w, h, title=None, cls="svg-region"):
    t = text(x + 16, y + 24, title, "svg-region-title", "start") if title else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="{cls}"/>' + t


def bar_chart(counts, years, label_j="Journal articles &amp; books", label_c="Conference papers"):
    W, H = 720, 270
    x0, x1, y0, y1 = 46, 706, 22, 222
    top = max([counts.get((y, "J"), 0) + counts.get((y, "C"), 0) for y in years] + [1])
    step = 5 if top > 10 else 2
    ymax = ((top + step - 1) // step) * step
    bw = (x1 - x0) / len(years)
    out = []
    for v in range(0, ymax + 1, step):
        y = y1 - (y1 - y0) * v / ymax
        out.append(f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" class="svg-grid"/>'
                   + text(x0 - 8, f"{y + 4:.1f}", v, "svg-axis", "end"))
    for i, yr in enumerate(years):
        j, c = counts.get((yr, "J"), 0), counts.get((yr, "C"), 0)
        cx, w = x0 + bw * i + bw / 2, bw * 0.62
        hj, hc = (y1 - y0) * j / ymax, (y1 - y0) * c / ymax
        out.append(f'<rect x="{cx - w / 2:.1f}" y="{y1 - hj:.1f}" width="{w:.1f}" height="{hj:.1f}" '
                   f'class="svg-bar-j"><title>{yr}: {j} journal</title></rect>')
        out.append(f'<rect x="{cx - w / 2:.1f}" y="{y1 - hj - hc:.1f}" width="{w:.1f}" height="{hc:.1f}" '
                   f'class="svg-bar-c"><title>{yr}: {c} conference</title></rect>')
        if j + c:
            out.append(text(f"{cx:.1f}", f"{y1 - hj - hc - 5:.1f}", j + c, "svg-value"))
        lab = yr if len(years) <= 14 or int(yr) % 2 == 0 else ""
        out.append(text(f"{cx:.1f}", y1 + 17, lab, "svg-axis"))
    out.append(f'<rect x="{x0 + 8}" y="{y0}" width="12" height="12" class="svg-bar-j"/>'
               + text(x0 + 26, y0 + 10, label_j, "svg-label", "start"))
    out.append(f'<rect x="{x0 + 200}" y="{y0}" width="12" height="12" class="svg-bar-c"/>'
               + text(x0 + 218, y0 + 10, label_c, "svg-label", "start"))
    return svg(W, H, "".join(out), "Papers per year", "Stacked bars of journal and conference papers per year.")
