#!/usr/bin/env python3
"""
Peer Educator — interactive lesson builder.

Emits a standalone trilingual lesson HTML file matching the ARISE lesson
contract exactly, so the forked PHP serves it with no special-casing:

  * body carries data-lesson-id / data-lesson-slug / data-module-slug
  * every string exists three times as .en / .sw / .sh spans
  * slide nav, language + text-size bar, scenario picker, MCQ/MSQ scoring
  * progress + score posted back to /peereducator/?p=api_lesson

Authoring is data, not markup: define slides as blocks and run

    python3 tools/build_lesson.py lessons/m01_peer_education.py
"""
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "template")


# ── trilingual helper ──────────────────────────────────────────────────
def T(t, block=False):
    """t is (en, sw, sh) or a plain str used for all three."""
    if isinstance(t, str):
        t = (t, t, t)
    en, sw, sh = t
    st = ' style="display:block;"' if block else ""
    return (f'<span class="en"{st}>{en}</span>'
            f'<span class="sw"{st}>{sw}</span>'
            f'<span class="sh"{st}>{sh}</span>')


def _esc(s):
    return html.escape(s, quote=True)


# ── block renderers ────────────────────────────────────────────────────
def b_p(b):
    return f'<p class="tp">{T(b["text"])}</p>'


def b_list(b):
    tag = "ol" if b.get("ordered") else "ul"
    items = "".join(f"<li>{T(i)}</li>" for i in b["items"])
    return f'<{tag} class="bl">{items}</{tag}>'


def b_table(b):
    head = "".join(f"<th>{T(h)}</th>" for h in b["headers"])
    rows = ""
    for r in b["rows"]:
        rows += "<tr>" + "".join(f"<td>{T(c)}</td>" for c in r) + "</tr>"
    return f'<table class="info-table"><tr>{head}</tr>{rows}</table>'


def b_key_term(b):
    return (f'<div class="key-term"><strong>{T(b["term"])}</strong>'
            f'{T(b["text"])}</div>')


def _boxed(cls, b):
    title = f'<strong>{T(b["title"])}</strong>' if b.get("title") else ""
    return f'<div class="{cls}">{title}{T(b["text"])}</div>'


def b_warn(b):    return _boxed("warn-box", b)
def b_tip(b):     return _boxed("tip-box", b)
def b_example(b): return _boxed("example-box", b)


def b_sheng(b):
    label = b.get("label", "Street Talk")
    return (f'<div class="sheng-box"><div class="sheng-head">{label}</div>'
            f'{T(b["text"], block=True)}</div>')


def b_facilitator(b):
    """Facilitator-only guidance: how to run this part, and for how long."""
    mins = f' · {b["minutes"]} min' if b.get("minutes") else ""
    return (f'<div class="fac-box"><div class="fac-head">'
            f'🎓 Facilitator note{mins}</div>{T(b["text"])}</div>')


def b_video(b):
    path = b.get("path", "")
    return ('<div class="video-slot">'
            '<video id="lessonVideo" controls style="display:none;width:100%;"></video>'
            '<div class="video-placeholder" id="videoPlaceholder">'
            '<div class="play-icon">🎬</div>'
            f'<p style="color:rgba(255,255,255,.8);">{_esc(b.get("caption","Module Video"))}</p>'
            '<p style="color:rgba(255,255,255,.6);font-size:.8rem;margin-top:6px;">'
            + T(("Your facilitator will upload this video.",
                 "Mwezeshaji wako ataipakia video hii.",
                 "Facilitator wako ata-upload hii video.")) +
            f'</p><span class="upload-note">📁 {_esc(path)}</span></div></div>')


def b_scenario(b, idx):
    sid = f"sc{idx}"
    choices, results = "", ""
    for n, ch in enumerate(b["choices"], 1):
        rid = f"{sid}r{n}"
        kind = ch["kind"]                     # good | bad
        choices += (f'<button class="choice" '
                    f'onclick="scPick(this,\'{sid}\',\'{kind}\',\'{rid}\')">'
                    f'{T(ch["text"])}</button>')
        retry = (f"<button class='retry-btn' onclick='scRetry(\"{sid}\")'>"
                 f"↩ Try Again</button>") if kind == "bad" else ""
        results += (f'<div class="s-result {kind}" id="{rid}">'
                    f'{T(ch["outcome"])}{retry}</div>')
    return (f'<div class="scenario-wrap" id="{sid}">'
            f'<div class="scenario-ctx">{T(b["context"])}</div>'
            f'<div class="scenario-q">{T(b["question"])}</div>'
            f'<div class="choices">{choices}</div>{results}</div>'
            f'<div style="margin-top:14px;"></div>')


RENDER = {"p": b_p, "list": b_list, "table": b_table, "key_term": b_key_term,
          "warn": b_warn, "tip": b_tip, "example": b_example,
          "sheng": b_sheng, "facilitator": b_facilitator, "video": b_video}


def render_blocks(blocks):
    out, sc = [], 0
    for b in blocks:
        t = b["type"]
        if t == "scenario":
            sc += 1
            out.append(b_scenario(b, sc))
        else:
            out.append(RENDER[t](b))
    return "".join(out)


# ── quiz ───────────────────────────────────────────────────────────────
def render_quiz(quiz):
    blocks, answers, explains, types = [], {}, {}, {}
    for i, q in enumerate(quiz, 1):
        gid = f"mcq{i}"
        multi = q.get("type", "mcq") == "msq"
        types[gid] = "msq" if multi else "mcq"
        answers[gid] = ",".join(q["answer"]) if multi else q["answer"]
        explains[gid] = q.get("explain", "")
        hint = ('<div style="font-size:.74rem;font-weight:700;color:#0a5e2a;margin-bottom:6px;">'
                "&#9745; Select ALL correct answers</div>" if multi else
                '<div style="font-size:.74rem;font-weight:700;color:#6b7280;margin-bottom:6px;">'
                "&#11044; Select ONE answer</div>")
        fn = "toggleOpt(this,'%s')" % gid if multi else "selectOpt(this,'%s','{L}')" % gid
        opts = ""
        for letter, text in zip("ABCDE", q["options"]):
            call = fn.replace("{L}", letter)
            opts += (f'<div class="opt" data-opt="{letter}" onclick="{call}">'
                     f'<span class="opt-letter">{letter}</span> {_esc(text)}</div>')
        blocks.append(f'<div class="mcq-block"><div class="q-text">{i}. {_esc(q["q"])}</div>'
                      f'{hint}<div class="options" id="{gid}">{opts}</div>'
                      f'<div class="mcq-fb" id="fb_{gid}"></div></div>')
    return "".join(blocks), answers, explains, types


# ── page ───────────────────────────────────────────────────────────────
def build(L):
    css = open(os.path.join(TPL, "lesson.css.html"), encoding="utf-8").read()
    js = open(os.path.join(TPL, "lesson.js.html"), encoding="utf-8").read()

    # facilitator-note styling is additive to the ARISE component set
    css = css.replace("</style>", """
.fac-box{background:#f3f0ff;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:11px 14px;margin:12px 0;font-size:.85rem;line-height:1.6;}
.fac-box .fac-head{color:#5b21b6;font-weight:700;font-size:.78rem;letter-spacing:.4px;margin-bottom:5px;text-transform:uppercase;}
.duration-pill{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.3);padding:2px 9px;border-radius:20px;font-size:.66rem;font-weight:700;margin-left:7px;white-space:nowrap;display:inline-block;}
/* keep the label + pill on one line; the pill must never orphan its unit */
.top-bar-left{min-width:0;flex:1;}
.top-bar-left .module-label{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.top-bar-left .lesson-name{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
</style>""")

    slides = []

    # slide 1 — objectives
    objs = "".join(f"<li>{T(o)}</li>" for o in L["objectives"])
    inq = (f'<div class="inquiry">{T(L["big_question"])}</div>'
           if L.get("big_question") else "")
    slides.append(
        '<div class="slide active"><div class="lo-box">'
        f'<h3>{T(("📋 By the end of this module:", "📋 Mwishoni mwa moduli hii:", "📋 Module hii ikiisha:"))}</h3>'
        f"<ol>{objs}</ol></div>{inq}</div>")

    # content slides
    for s in L["slides"]:
        icon = s.get("icon", "")
        slides.append(f'<div class="slide"><div class="slide-head">{icon} '
                      f'{T(s["head"])}</div>{render_blocks(s["blocks"])}</div>')

    # quiz slide
    qhtml, answers, explains, types = render_quiz(L["quiz"])
    n = len(L["quiz"])
    slides.append(
        '<div class="slide"><div class="slide-head">&#128221; '
        + T((f"Knowledge Check — {n} Questions", f"Maswali ya Kupima — {n}",
             f"Knowledge Check — {n} Questions")) + "</div>"
        '<div style="font-size:.78rem;color:#6b7280;margin-bottom:12px;">'
        + T(("Answer all questions, then tap <strong>Submit</strong>.",
             "Jibu maswali yote, kisha bonyeza <strong>Wasilisha</strong>.",
             "Answer maswali yote, then tap <strong>Submit</strong>.")) + "</div>"
        + qhtml +
        '<button class="check-btn" onclick="submitMCQ()">'
        + T(("Submit Answers", "Wasilisha Majibu", "Submit Answers")) + "</button>"
        '<div class="score-box" id="score-box" style="display:none;">'
        '<div class="score-num" id="score-title"></div>'
        '<div id="score-detail"></div></div></div>')

    # Wire the generated answer keys into the shared script.
    # Lambda replacements: json.dumps emits \uXXXX, which re.sub would
    # otherwise try to interpret as template escapes.
    import re
    for var, val in (("mcqAnswers", answers), ("mcqExplain", explains), ("mcqTypes", types)):
        payload = "var %s=%s;" % (var, json.dumps(val, ensure_ascii=False))
        js, n = re.subn(r"var %s=\{.*?\};" % var, lambda _m, p=payload: p, js, count=1)
        if n != 1:
            raise RuntimeError("could not wire %s into the lesson script" % var)

    dur = (f'<span class="duration-pill">⏱ {L["duration"]} min</span>'
           if L.get("duration") else "")

    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{_esc(L['title'])} | Peer Educator</title>{css}
</head>
<body data-lesson-id="0" data-lesson-slug="{_esc(L['lesson_slug'])}" data-module-slug="{_esc(L['module_slug'])}">
<div class="top-bar"><div class="top-bar-left"><div class="module-label">{_esc(L['module_label'])}{dur}</div><div class="lesson-name">{L.get('icon','')} {_esc(L['title'])}</div></div><span class="slide-badge" id="slideCounter">1 / {len(slides)}</span></div>
<div class="lang-bar"><div class="lang-bar-inner"><span class="lb-label">🌍</span><button class="lb-btn active" id="enBtn" onclick="setLang('en')">EN</button><button class="lb-btn" id="swBtn" onclick="setLang('sw')">SW</button><button class="lb-btn" id="shBtn" onclick="setLang('sh')">SH</button><span class="lb-sep">|</span><span class="lb-label">🔡</span><button class="lb-size-btn active" id="sz-sm" onclick="setSize('sm')">A−</button><button class="lb-size-btn" id="sz-md" onclick="setSize('md')">A</button><button class="lb-size-btn" id="sz-lg" onclick="setSize('lg')">A+</button><a href="/peereducator/?p=resources" class="lb-help">🆘 Help</a></div></div>
<div class="slides-wrap" id="slidesWrap">{''.join(slides)}</div>
{js}
</body>
</html>
"""


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: build_lesson.py <lesson_module.py> [more...]")
    outdir = os.path.join(os.path.dirname(HERE), "data", "uploads", "interactive")
    os.makedirs(outdir, exist_ok=True)
    for path in sys.argv[1:]:
        ns = {}
        exec(open(path, encoding="utf-8").read(), ns)
        L = ns["LESSON"]
        out = os.path.join(outdir, L["file"])
        html_out = build(L)
        open(out, "w", encoding="utf-8").write(html_out)
        nslides = html_out.count('<div class="slide">') + html_out.count('<div class="slide active">')
        print(f"  {L['file']:<44} {len(html_out):>7,} bytes  "
              f"{nslides} slides  {len(L['quiz'])} questions")


if __name__ == "__main__":
    main()
