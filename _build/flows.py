"""Coded user-flow diagrams (inline SVG). Sharp at any size, styled by assets/style.css (.flow)."""

NW, NH = 184, 62                 # step / status node size
GAP = 76                         # horizontal gap between nodes
STEP = NW + GAP
C = [100 + i * STEP for i in range(7)]   # column centres
R1, RM, R2 = 118, 232, 346               # row centres (top, middle, bottom)
W, H = C[-1] + NW / 2 + 24, 430


def _rect(cx, cy, w=NW, h=NH, cls="step", rx=12):
    return f'<rect class="{cls}" x="{cx - w/2}" y="{cy - h/2}" width="{w}" height="{h}" rx="{rx}"/>'


def _text(cx, cy, lines, cls="t"):
    n = len(lines)
    return "".join(f'<text class="{cls}" x="{cx}" y="{cy + (i - (n - 1) / 2) * 18 + 5}" text-anchor="middle">{l}</text>'
                   for i, l in enumerate(lines))


def start(cx, cy, label):
    w = 168
    x0 = cx - w / 2
    tw = len(label) * 7.7            # approx. text width at 14px
    gx = cx - (tw + 20) / 2          # centre "+ label" as one group
    return (f'<g><rect class="start" x="{x0}" y="{cy - 24}" width="{w}" height="48" rx="24"/>'
            f'<path class="plus" d="M{gx} {cy}h10M{gx + 5} {cy - 5}v10"/>'
            f'<text class="t-start" x="{gx + 20}" y="{cy + 5}">{label}</text></g>')


def step(cx, cy, lines):
    return f'<g>{_rect(cx, cy)}{_text(cx, cy, lines)}</g>'


CHIPS = {"Draft": ("chip-draft", 56), "Published": ("chip-pub", 82), "Pending": ("chip-pend", 70),
         "Inactive": ("chip-off", 70), "Sent": ("chip-pub", 50)}


def status(cx, cy, kind, subject, locked=False, sub=None):
    x0, top = cx - NW / 2, cy - NH / 2
    cls, chip_w = CHIPS[kind]
    xc = x0 + NW - 14 - chip_w
    lock = (f'<rect class="lock" x="{x0 + 16}" y="{cy + 9}" width="9" height="7" rx="1.5"/>'
            f'<path class="lock" d="M{x0 + 18} {cy + 9}v-2.5a2.5 2.5 0 0 1 5 0V{cy + 9}"/>') if locked else ""
    if sub is None:
        sub = "Locked for editing" if locked else "Editable"
    return (f'<g>{_rect(cx, cy, cls="status")}'
            f'<text class="t" x="{x0 + 16}" y="{top + 26}">{subject}</text>'
            f'<rect class="{cls}" x="{xc}" y="{top + 12}" width="{chip_w}" height="20" rx="10"/>'
            f'<text class="t-chip {cls}-t" x="{xc + chip_w/2}" y="{top + 25.5}" text-anchor="middle">{kind.upper()}</text>'
            f'{lock}<text class="t-sub" x="{x0 + (32 if locked else 16)}" y="{cy + 17}">{sub}</text></g>')


def decision(cx, cy, lines):
    w, h = NW, 74
    return (f'<g>{_rect(cx, cy, w, h, "decision", 37)}'
            f'<path class="dia" d="M{cx - w/2 + 24} {cy}l7-7 7 7-7 7z"/>'
            f'{_text(cx + 12, cy, lines, "t-dec")}</g>')


def action(cx, cy, lines):
    return f'<g>{_rect(cx, cy, NW, NH, "action", 31)}{_text(cx, cy, lines, "t-action")}</g>'


def path(d, red=False, back=False):
    cls = "e no" if red else ("e back" if back else "e")
    return f'<path class="{cls}" d="{d}" marker-end="url(#{"ah-red" if red else "ah"})"/>'


def elbow(x1, y1, x2, y2, xm, r=14):
    """Horizontal → vertical → horizontal connector with rounded corners."""
    s = 1 if y2 > y1 else -1
    return (f"M{x1} {y1}H{xm - r}Q{xm} {y1} {xm} {y1 + s*r}"
            f"V{y2 - s*r}Q{xm} {y2} {xm + r} {y2}H{x2}")


def loop(x1, x2, y_from, y_lane, r=12):
    """Vertical out of one node, along a lane, vertical into another (used for No / Cancel)."""
    s = 1 if y_lane > y_from else -1
    d = -1 if x2 < x1 else 1
    return (f"M{x1} {y_from}V{y_lane - s*r}Q{x1} {y_lane} {x1 + d*r} {y_lane}"
            f"H{x2 - d*r}Q{x2} {y_lane} {x2} {y_lane - s*r}V{y_from + s*6}")


def label(x, y, txt, red=False, grey=False):
    cls = "lbl-no" if red else ("lbl-grey" if grey else "lbl-yes")
    w = 14 + len(txt) * 7
    return (f'<rect class="{cls}" x="{x - w/2}" y="{y - 11}" width="{w}" height="22" rx="11"/>'
            f'<text class="{cls}-t" x="{x}" y="{y + 4}" text-anchor="middle">{txt}</text>')


def nft_flow():
    hw, e, lbl = NW / 2, [], []
    gap_mid = lambda a, b: (C[a] + hw + C[b] - hw) / 2
    # rows 1 & 2: start -> define -> draft
    for r in (R1, R2):
        e.append(path(f"M{C[0] + 84} {r}H{C[1] - hw - 3}")); lbl.append(label((C[0] + 84 + C[1] - hw) / 2, r, "Yes"))
        e.append(path(f"M{C[1] + hw} {r}H{C[2] - hw - 3}"))
    # drafts merge into the decision
    trunk1 = (C[2] + hw + C[3] - hw) / 2
    e.append(path(elbow(C[2] + hw, R1, C[3] - hw - 3, RM, trunk1)))
    e.append(path(elbow(C[2] + hw, R2, C[3] - hw - 3, RM, trunk1)))
    # decision -> publish
    e.append(path(f"M{C[3] + hw} {RM}H{C[4] - hw - 3}")); lbl.append(label(gap_mid(3, 4), RM, "Yes"))
    # publish splits to published collection / item
    trunk2 = (C[4] + hw + C[5] - hw) / 2
    e.append(path(elbow(C[4] + hw, RM, C[5] - hw - 3, R1, trunk2)))
    e.append(path(elbow(C[4] + hw, RM, C[5] - hw - 3, R2, trunk2)))
    # published collection -> associate more items, and No back
    e.append(path(f"M{C[5] + hw} {R1}H{C[6] - hw - 3}")); lbl.append(label(gap_mid(5, 6), R1, "Yes"))
    e.append(path(loop(C[6], C[5], R1 + NH / 2, R1 + 70), red=True)); lbl.append(label((C[5] + C[6]) / 2, R1 + 70, "No", red=True))
    # cancel: published collection back to draft
    e.append(path(loop(C[5], C[2], R1 - NH / 2, R1 - 76), red=True)); lbl.append(label((C[2] + C[5]) / 2, R1 - 76, "Cancel", red=True))
    # published item -> marketplace
    e.append(path(f"M{C[5] + hw} {R2}H{C[6] - hw - 3}"))

    nodes = [
        start(C[0], R1, "Add collection"), step(C[1], R1, ["Define properties"]), status(C[2], R1, "Draft", "Collection"),
        start(C[0], R2, "Add item"), step(C[1], R2, ["Define properties"]), status(C[2], R2, "Draft", "Item"),
        decision(C[3], RM, ["Associate or", "remove items?"]), action(C[4], RM, ["Publish collection"]),
        status(C[5], R1, "Published", "Collection", locked=True), step(C[6], R1, ["Associate more items"]),
        status(C[5], R2, "Published", "Item", locked=True), step(C[6], R2, ["Add / remove from", "marketplace"]),
    ]
    defs = DEFS
    return (f'<svg class="flow-svg" viewBox="0 0 {W:.0f} {H}" style="--w:{W:.0f}" role="img" '
            f'aria-label="User flow: creating collections and items, from draft to published">'
            f'{defs}{"".join(e)}{"".join(nodes)}{"".join(lbl)}</svg>')


DEFS = ('<defs>'
            '<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1l7 4-7 4" class="ah"/></marker>'
            '<marker id="ah-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1l7 4-7 4" class="ah-red"/></marker>'
            '</defs>')


def svg(w, h, label_txt, parts):
    return (f'<svg class="flow-svg" viewBox="0 0 {w:.0f} {h}" style="--w:{w:.0f}" role="img" aria-label="{label_txt}">'
            f'{DEFS}{"".join(parts)}</svg>')


def beneficiary_flow():
    hw = NW / 2
    c = [100 + i * STEP for i in range(6)]
    r1, r2, r3 = 112, 250, 352
    e, lbl = [], []
    # main path
    e.append(path(f"M{c[0] + 84} {r1}H{c[1] - hw - 3}"))
    e.append(path(f"M{c[1] + hw} {r1}H{c[2] - hw - 3}"))
    e.append(path(f"M{c[2] + hw} {r1}H{c[3] - hw - 3}")); lbl.append(label((c[2] + c[3]) / 2, r1, "Yes"))
    e.append(path(f"M{c[3] + hw} {r1}H{c[4] - hw - 3}"))
    e.append(path(f"M{c[4] + hw} {r1}H{c[5] - hw - 3}")); lbl.append(label((c[4] + c[5]) / 2, r1, "Approved"))
    # reject -> not active
    trunk = (c[4] + hw + c[5] - hw) / 2
    e.append(path(f"M{c[4]} {r1 + 37}V{r2 - 12}Q{c[4]} {r2} {c[4] + 12} {r2}H{c[5] - hw - 3}", red=True)); lbl.append(label(c[4] + 70, r2, "Reject", red=True))
    # cancel back to start
    e.append(path(loop(c[2], c[0], r1 - 37, r1 - 70), red=True)); lbl.append(label((c[0] + c[2]) / 2, r1 - 70, "Cancel", red=True))
    # existing beneficiaries branch
    tr = (c[0] + 84 + c[1] - hw) / 2
    e.append(path(f"M{c[0]} {r1 + 24}V{r2 - 14}Q{c[0]} {r2} {c[0] + 14} {r2}H{c[1] - hw - 3}"))
    t2 = (c[1] + hw + c[2] - hw) / 2
    e.append(path(f"M{c[1] + hw} {r2}H{c[2] - hw - 3}"))
    e.append(path(elbow(c[1] + hw, r2, c[2] - hw - 3, r3, t2)))
    nodes = [
        start(c[0], r1, "Beneficiaries"), step(c[1], r1, ["“Add beneficiary”"]),
        decision(c[2], r1, ["Add beneficiary", "details"]),
        status(c[3], r1, "Pending", "Beneficiary", sub="Awaiting approval"),
        decision(c[4], r1, ["Back-office", "review"]), action(c[5], r1, ["Pay beneficiary"]),
        status(c[5], r2, "Inactive", "Beneficiary", sub="Rejected"),
        step(c[1], r2, ["Active beneficiary"]), step(c[2], r2, ["Pay"]), step(c[2], r3, ["View profile"]),
    ]
    W = c[-1] + hw + 24
    return svg(W, 410, "User flow: adding a beneficiary, with back-office approval", e + nodes + lbl)


def pending_flow():
    hw = NW / 2
    c = [100 + i * STEP for i in range(6)]
    rt, rm, rb, rl = 96, 210, 324, 420
    lane = c[5] + hw + 36
    e, lbl = [], []
    e.append(path(f"M{c[0] + 84} {rm}H{c[1] - hw - 3}"))
    e.append(path(f"M{c[1] + hw} {rm}H{c[2] - hw - 3}"))
    e.append(path(f"M{c[2] + hw} {rm}H{c[3] - hw - 3}")); lbl.append(label((c[2] + c[3]) / 2, rm, "Yes"))
    t = (c[3] + hw + c[4] - hw) / 2
    e.append(path(elbow(c[3] + hw, rm, c[4] - hw - 3, rt, t)))
    e.append(path(f"M{c[3] + hw} {rm}H{c[4] - hw - 3}"))
    e.append(path(elbow(c[3] + hw, rm, c[4] - hw - 3, rb, t)))
    # edit -> decision
    e.append(path(f"M{c[4] + hw} {rt}H{c[5] - hw - 3}"))
    # approve -> sent ; reject payment -> activity
    e.append(path(f"M{c[4] + hw} {rm}H{c[5] - hw - 3}")); lbl.append(label((c[4] + c[5]) / 2, rm, "Yes"))
    e.append(path(f"M{c[4] + hw} {rb}H{c[5] - hw - 3}")); lbl.append(label((c[4] + c[5]) / 2, rb, "Yes"))
    # approve: No -> activity
    e.append(path(f"M{c[4]} {rm + NH/2}V{rm + 45}Q{c[4]} {rm + 57} {c[4] + 12} {rm + 57}H{c[5] - 12}Q{c[5]} {rm + 57} {c[5]} {rm + 69}V{rb - NH/2 - 4}", red=True))
    lbl.append(label((c[4] + c[5]) / 2 + 30, rm + 57, "No", red=True))
    # decision: reject -> activity (via right lane)
    e.append(path(f"M{c[5] + hw} {rt}H{lane - 12}Q{lane} {rt} {lane} {rt + 12}V{rb - 12}Q{lane} {rb} {lane - 12} {rb}H{c[5] + hw + 4}", red=True))
    lbl.append(label(lane, (rt + rb) / 2, "Reject", red=True))
    # open pending request branch
    e.append(path(f"M{c[0]} {rm + 24}V{rl - 14}Q{c[0]} {rl} {c[0] + 14} {rl}H{c[1] - hw - 3}"))
    e.append(path(f"M{c[1] + hw} {rl}H{c[2] - hw - 3}"))
    e.append(path(loop(c[2], c[1], rl + NH / 2, rl + 62), back=True)); lbl.append(label((c[1] + c[2]) / 2, rl + 62, "Go back", grey=True))
    nodes = [
        start(c[0], rm, "Pending requests"), step(c[1], rm, ["Awaiting authorization"]),
        decision(c[2], rm, ["Found awaiting", "requests?"]), step(c[3], rm, ["Select awaiting", "payment"]),
        step(c[4], rt, ["Edit"]), step(c[4], rm, ["Approve payment"]), step(c[4], rb, ["Reject payment"]),
        decision(c[5], rt, ["Reject or", "approve?"]),
        status(c[5], rm, "Sent", "Final approval", sub="In the admin system"),
        action(c[5], rb, ["Activity page"]),
        step(c[1], rl, ["Open pending request"]), step(c[2], rl, ["View pending request"]),
    ]
    W = lane + 40
    return svg(W, 500, "User flow: handling pending payment requests", e + nodes + lbl)

