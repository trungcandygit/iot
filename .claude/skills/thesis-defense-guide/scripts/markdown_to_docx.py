#!/usr/bin/env python3
"""Convert a defense-guide Markdown file into a styled DOCX.

This is intentionally dependency-free: it writes a minimal OpenXML package using
only the Python standard library. It supports headings, bullets, numbered lists,
quotes, evaluator sections, question headings, dialogue labels, and answer boxes.
"""

from __future__ import annotations

import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_REL = "http://schemas.openxmlformats.org/package/2006/relationships"

ZH_QUESTION = "\u95ee\u9898"
ZH_RECOMMENDED_ANSWER = "\u63a8\u8350\u56de\u7b54\uff1a"
ZH_CONTINUE_ANSWER = "\u7ee7\u7eed\u56de\u7b54\uff1a"
ZH_QUESTION_INTENT = "\u25b6 \u95ee\u9898\u610f\u56fe"
ZH_REFERENCE_ANSWER = "\u25b6 \u53c2\u8003\u56de\u7b54"
ZH_BONUS_POINT = "\u25b6 \u52a0\u5206\u70b9"
ZH_IF_CHALLENGED = "\u25b6 \u82e5\u88ab\u8ffd\u95ee"
ZH_POTENTIAL_CONCERN = "\u3010\u6f5c\u5728\u5173\u5207\u70b9\u3011"
ZH_TEN_SECOND_ANSWER = "\u25b6 10\u79d2\u56de\u7b54"
ZH_THIRTY_SECOND_ANSWER = "\u25b6 30\u79d2\u56de\u7b54"
ZH_SIXTY_SECOND_ANSWER = "\u25b6 60\u79d2\u56de\u7b54"
ZH_EVIDENCE_LEVEL = "\u25b6 \u8bc1\u636e\u7b49\u7ea7"
ZH_STAGE_STRATEGY = "\u25b6 \u7b54\u8fa9\u9636\u6bb5\u7b56\u7565"
ZH_ANTI_OVERCLAIM_CHECK = "\u25b6 \u9632\u8fc7\u5ea6\u627f\u8bfa\u68c0\u67e5"
ZH_SAFER_WORDING = "\u25b6 \u66f4\u7a33\u59a5\u8bf4\u6cd5"
ZH_DO_NOT_SAY = "\u25b6 \u4e0d\u8981\u8fd9\u6837\u8bf4"
ZH_IF_CONTINUE = "\u5982\u679c\u7ee7\u7eed\u8ffd\u95ee"
ZH_DO_NOT = "\u4e0d\u8981"
ZH_STEADIER = "\u66f4\u7a33"
ZH_TEACHER = "\u8001\u5e08"
ZH_TEACHER_PREFIX = "\u8001\u5e08\uff1a"
ZH_STUDENT_PREFIX = "\u4f60\uff1a"
ZH_COLON = "\uff1a"

ANSWER_LABEL_PREFIXES = (
    "recommended answer:",
    "answer:",
    "\u25b6 reference answer",
    "\u25b6 10-second answer",
    "\u25b6 30-second answer",
    "\u25b6 60-second answer",
)

INFO_LABEL_PREFIXES = (
    "follow-up",
    "bonus point",
    "question intent",
    "evidence level",
    "defense stage strategy",
    "anti-overclaiming check",
    "safer wording",
    "do not say",
    "if challenged further",
    "if cornered",
    "\u25b6 question intent",
    "\u25b6 bonus point",
    "\u25b6 if challenged further",
    "\u25b6 evidence level",
    "\u25b6 defense stage strategy",
    "\u25b6 anti-overclaiming check",
    "\u25b6 safer wording",
    "\u25b6 do not say",
)


def run(text: str, *, bold: bool = False, italic: bool = False, color: str | None = None, size: int | None = None, code: bool = False) -> str:
    props: list[str] = []
    if code:
        props.append('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:eastAsia="Microsoft YaHei"/>')
        props.append('<w:color w:val="7C2D12"/>')
    else:
        props.append('<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/>')
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    if color:
        props.append(f'<w:color w:val="{color}"/>')
    if size:
        props.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    space = ' xml:space="preserve"' if text.startswith(" ") or text.endswith(" ") else ""
    return f'<w:r><w:rPr>{"".join(props)}</w:rPr><w:t{space}>{escape(text)}</w:t></w:r>'


def inline_runs(text: str, default_color: str | None = None) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f"{m.group(1)} ({m.group(2)})", text)
    out: list[str] = []
    pos = 0
    for match in re.finditer(r"(\*\*([^*]+)\*\*|`([^`]+)`)", text):
        if match.start() > pos:
            out.append(run(text[pos : match.start()], color=default_color))
        if match.group(2):
            out.append(run(match.group(2), bold=True, color=default_color))
        else:
            out.append(run(match.group(3), code=True))
        pos = match.end()
    if pos < len(text):
        out.append(run(text[pos:], color=default_color))
    return "".join(out) if out else run("", color=default_color)


def ppr(
    *,
    style: str | None = None,
    jc: str | None = None,
    shade: str | None = None,
    before: int | None = None,
    after: int | None = None,
    line: int | None = 300,
    indent_left: int | None = None,
    hanging: int | None = None,
    keep_next: bool = False,
    page_break_before: bool = False,
) -> str:
    props: list[str] = []
    if style:
        props.append(f'<w:pStyle w:val="{style}"/>')
    if keep_next:
        props.append("<w:keepNext/>")
    if page_break_before:
        props.append("<w:pageBreakBefore/>")
    if jc:
        props.append(f'<w:jc w:val="{jc}"/>')
    if shade:
        props.append(f'<w:shd w:fill="{shade}"/>')
    spacing: list[str] = []
    if before is not None:
        spacing.append(f'w:before="{before}"')
    if after is not None:
        spacing.append(f'w:after="{after}"')
    if line is not None:
        spacing.append(f'w:line="{line}" w:lineRule="auto"')
    if spacing:
        props.append(f'<w:spacing {" ".join(spacing)}/>')
    ind: list[str] = []
    if indent_left is not None:
        ind.append(f'w:left="{indent_left}"')
    if hanging is not None:
        ind.append(f'w:hanging="{hanging}"')
    if ind:
        props.append(f'<w:ind {" ".join(ind)}/>')
    return f'<w:pPr>{"".join(props)}</w:pPr>' if props else ""


def para(
    text: str = "",
    *,
    style: str = "Normal",
    bold: bool = False,
    italic: bool = False,
    color: str | None = None,
    size: int | None = None,
    jc: str | None = None,
    shade: str | None = None,
    bullet: bool = False,
    before: int | None = None,
    after: int | None = None,
    keep_next: bool = False,
    page_break_before: bool = False,
) -> str:
    body = run(text, bold=bold, italic=italic, color=color, size=size) if (bold or italic or color or size) else inline_runs(text)
    prefix = run("- ", bold=True, color=color) if bullet else ""
    paragraph_props = ppr(
        style=style,
        jc=jc,
        shade=shade,
        before=before,
        after=after,
        indent_left=420 if bullet else None,
        hanging=180 if bullet else None,
        keep_next=keep_next,
        page_break_before=page_break_before,
    )
    return f"<w:p>{paragraph_props}{prefix}{body}</w:p>"


def para_runs(runs: list[str], *, style: str = "Normal", before: int | None = None, after: int | None = None, indent_left: int | None = None) -> str:
    return f'<w:p>{ppr(style=style, before=before, after=after, indent_left=indent_left)}{"".join(runs)}</w:p>'


def page_break() -> str:
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def cell(content: str, *, fill: str = "FFFFFF", width: str = "3000") -> str:
    return f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/><w:shd w:fill="{fill}"/></w:tcPr>{content}</w:tc>'


def is_table_line(text: str) -> bool:
    return text.startswith("|") and text.endswith("|") and text.count("|") >= 2


def split_table_row(text: str) -> list[str]:
    return [item.strip() for item in text.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    col_count = max(len(row) for row in rows)
    col_width = max(1200, 9360 // max(1, col_count))
    grid = "".join(f'<w:gridCol w:w="{col_width}"/>' for _ in range(col_count))
    rendered_rows: list[str] = []
    for row_index, row in enumerate(rows):
        cells: list[str] = []
        for col_index in range(col_count):
            text = row[col_index] if col_index < len(row) else ""
            fill = "E2E8F0" if row_index == 0 else "FFFFFF"
            cells.append(cell(para(text, bold=row_index == 0, after=40), fill=fill, width=str(col_width)))
        rendered_rows.append(f'<w:tr>{"".join(cells)}</w:tr>')
    return (
        f'<w:tbl><w:tblPr><w:tblW w:w="9360" w:type="dxa"/>'
        f'<w:tblBorders><w:top w:val="single" w:sz="6" w:color="CBD5E1"/>'
        f'<w:left w:val="single" w:sz="6" w:color="CBD5E1"/>'
        f'<w:bottom w:val="single" w:sz="6" w:color="CBD5E1"/>'
        f'<w:right w:val="single" w:sz="6" w:color="CBD5E1"/>'
        f'<w:insideH w:val="single" w:sz="4" w:color="E2E8F0"/>'
        f'<w:insideV w:val="single" w:sz="4" w:color="E2E8F0"/></w:tblBorders>'
        f'<w:tblCellMar><w:top w:w="80" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
        f'<w:bottom w:w="70" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar>'
        f'</w:tblPr><w:tblGrid>{grid}</w:tblGrid>{"".join(rendered_rows)}</w:tbl>'
    )


def callout(paragraphs: list[str], *, fill: str = "F8FAFC", border: str = "CBD5E1") -> str:
    inner = "".join(para(item, style="Normal") for item in paragraphs)
    return (
        f'<w:tbl><w:tblPr><w:tblW w:w="9360" w:type="dxa"/>'
        f'<w:tblBorders><w:top w:val="single" w:sz="8" w:color="{border}"/>'
        f'<w:left w:val="single" w:sz="18" w:color="{border}"/>'
        f'<w:bottom w:val="single" w:sz="8" w:color="{border}"/>'
        f'<w:right w:val="single" w:sz="8" w:color="{border}"/></w:tblBorders>'
        f'<w:tblCellMar><w:top w:w="150" w:type="dxa"/><w:left w:w="180" w:type="dxa"/>'
        f'<w:bottom w:w="130" w:type="dxa"/><w:right w:w="180" w:type="dxa"/></w:tblCellMar>'
        f'</w:tblPr><w:tblGrid><w:gridCol w:w="9360"/></w:tblGrid><w:tr>{cell(inner, fill=fill, width="9360")}</w:tr></w:tbl>'
    )


def styles_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{NS_W}">
  <w:docDefaults>
    <w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/><w:sz w:val="21"/><w:szCs w:val="21"/><w:color w:val="1F2937"/></w:rPr></w:rPrDefault>
    <w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="300" w:lineRule="auto"/></w:pPr></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/><w:b/><w:color w:val="0F172A"/><w:sz w:val="40"/><w:szCs w:val="40"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="CoverSub"><w:name w:val="CoverSub"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/><w:color w:val="475569"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="CoverNote"><w:name w:val="CoverNote"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/><w:b/><w:color w:val="1D4ED8"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="420" w:after="220"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/><w:b/><w:color w:val="0F172A"/><w:sz w:val="30"/><w:szCs w:val="30"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="280" w:after="140"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/><w:b/><w:color w:val="1E3A8A"/><w:sz w:val="25"/><w:szCs w:val="25"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="220" w:after="100"/><w:outlineLvl w:val="2"/></w:pPr><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Microsoft YaHei"/><w:b/><w:color w:val="334155"/><w:sz w:val="23"/><w:szCs w:val="23"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="SectionTitle"><w:name w:val="SectionTitle"/><w:basedOn w:val="Normal"/><w:qFormat/></w:style>
  <w:style w:type="paragraph" w:styleId="Question"><w:name w:val="Question"/><w:basedOn w:val="Normal"/><w:qFormat/></w:style>
  <w:style w:type="paragraph" w:styleId="Label"><w:name w:val="Label"/><w:basedOn w:val="Normal"/><w:qFormat/></w:style>
  <w:style w:type="paragraph" w:styleId="Dialogue"><w:name w:val="Dialogue"/><w:basedOn w:val="Normal"/><w:qFormat/></w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="420" w:hanging="180"/></w:pPr></w:style>
</w:styles>'''


def starts_with_any(text: str, prefixes: tuple[str, ...]) -> bool:
    lower = text.lower()
    return any(lower.startswith(prefix) for prefix in prefixes)


def is_answer_label(text: str) -> bool:
    return (
        starts_with_any(text, ANSWER_LABEL_PREFIXES)
        or text in {ZH_RECOMMENDED_ANSWER, ZH_CONTINUE_ANSWER}
        or text.startswith(ZH_REFERENCE_ANSWER)
        or text.startswith(ZH_TEN_SECOND_ANSWER)
        or text.startswith(ZH_THIRTY_SECOND_ANSWER)
        or text.startswith(ZH_SIXTY_SECOND_ANSWER)
    )


def is_info_label(text: str) -> bool:
    return (
        starts_with_any(text, INFO_LABEL_PREFIXES)
        or text.startswith(ZH_QUESTION_INTENT)
        or text.startswith(ZH_BONUS_POINT)
        or text.startswith(ZH_IF_CHALLENGED)
        or text.startswith(ZH_EVIDENCE_LEVEL)
        or text.startswith(ZH_STAGE_STRATEGY)
        or text.startswith(ZH_ANTI_OVERCLAIM_CHECK)
        or text.startswith(ZH_SAFER_WORDING)
        or text.startswith(ZH_DO_NOT_SAY)
        or text.startswith(ZH_IF_CONTINUE)
        or text.startswith(ZH_DO_NOT)
        or text.startswith(ZH_STEADIER)
    )


def build_doc(markdown: str, title: str) -> str:
    lines = markdown.splitlines()
    first_heading = next((re.match(r"^#\s+(.*)$", line.strip()).group(1) for line in lines if re.match(r"^#\s+", line.strip())), title)
    body: list[str] = []
    body.append(para(first_heading, style="Title", jc="center", before=1000, after=330))
    body.append(para(title, style="CoverNote", jc="center", after=460))
    body.append(callout([
        "Use by evaluator: review each committee member's section, then practice the chain follow-up scripts.",
        "Answer principle: qualify claims, admit limits, and defend the contribution without overclaiming.",
    ], fill="EEF6FF", border="2563EB"))
    body.append(page_break())

    colors = ["1E3A8A", "7C2D12", "166534", "5B21B6", "0F766E"]
    section_index = -1
    skip_first_h1 = True
    pending_answer: list[str] = []
    in_answer = False

    def flush_answer() -> None:
        nonlocal in_answer
        if pending_answer:
            body.append(callout(list(pending_answer), fill="F8FAFC", border="CBD5E1"))
            pending_answer.clear()
        in_answer = False

    idx = 0
    while idx < len(lines):
        raw = lines[idx]
        text = raw.rstrip().strip()
        if not text:
            flush_answer()
            idx += 1
            continue
        if is_table_line(text):
            flush_answer()
            rows: list[list[str]] = []
            while idx < len(lines):
                candidate = lines[idx].rstrip().strip()
                if not is_table_line(candidate):
                    break
                cells = split_table_row(candidate)
                if not is_separator_row(cells):
                    rows.append(cells)
                idx += 1
            body.append(markdown_table(rows))
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", text)
        if heading:
            flush_answer()
            level = len(heading.group(1))
            heading_text = heading.group(2).strip()
            if level == 1 and skip_first_h1:
                skip_first_h1 = False
                idx += 1
                continue
            if level == 1:
                section_index += 1
                body.append(para(heading_text, style="SectionTitle", bold=True, color="FFFFFF", size=32, shade=colors[section_index % len(colors)], before=280, after=260, page_break_before=True))
            elif level == 2:
                body.append(para(heading_text, style="Heading2", keep_next=True))
            else:
                is_question = "question" in heading_text.lower() or ZH_QUESTION in heading_text
                body.append(para(heading_text, style="Question" if is_question else "Heading3", bold=is_question, color="0F172A" if is_question else None, shade="E0F2FE" if is_question else None, before=220, after=120, keep_next=True))
            idx += 1
            continue
        if text.startswith(">"):
            flush_answer()
            body.append(callout([text.lstrip(">").strip()], fill="EFF6FF", border="2563EB"))
            idx += 1
            continue
        if text.startswith(ZH_POTENTIAL_CONCERN) or text.startswith("\u3010Potential concern\u3011"):
            flush_answer()
            body.append(callout([text], fill="FFF7ED", border="F97316"))
            idx += 1
            continue
        if is_answer_label(text):
            flush_answer()
            in_answer = True
            body.append(para(text, style="Label", bold=True, color="166534", before=140, after=40))
            idx += 1
            continue
        if is_info_label(text):
            flush_answer()
            body.append(para(text, style="Label", bold=True, color="B45309", before=140, after=40))
            idx += 1
            continue
        if text.startswith("Evaluator:") or text.startswith("Student:") or text.startswith(ZH_TEACHER_PREFIX) or text.startswith(ZH_STUDENT_PREFIX):
            flush_answer()
            if ":" in text:
                label, rest = text.split(":", 1)
                sep = ":"
            elif ZH_COLON in text:
                label, rest = text.split(ZH_COLON, 1)
                sep = ZH_COLON
            else:
                label, rest, sep = text[:2], text[2:], ""
            teacher_label = label.lower().startswith("evaluator") or label == ZH_TEACHER
            body.append(para_runs([run(label + sep, bold=True, color="B91C1C" if teacher_label else "166534"), run(rest)], style="Dialogue", before=80, after=60, indent_left=240))
            idx += 1
            continue
        bullet = re.match(r"^[-*]\s+(.*)$", text)
        numbered = re.match(r"^(\d+)\.\s+(.*)$", text)
        if bullet:
            if in_answer:
                pending_answer.append("- " + bullet.group(1).strip())
            else:
                body.append(para(bullet.group(1).strip(), style="ListParagraph", bullet=True))
            idx += 1
            continue
        if numbered:
            line = f"{numbered.group(1)}. {numbered.group(2)}"
            if in_answer:
                pending_answer.append(line)
            else:
                body.append(para(line, style="ListParagraph"))
            idx += 1
            continue
        if in_answer:
            pending_answer.append(text)
        else:
            body.append(para(text, style="Normal"))
        idx += 1

    flush_answer()
    sect = '<w:sectPr><w:headerReference w:type="default" r:id="rIdHeader"/><w:footerReference w:type="default" r:id="rIdFooter"/><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080" w:header="540" w:footer="540" w:gutter="0"/></w:sectPr>'
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="{NS_W}" xmlns:r="{NS_R}"><w:body>{"".join(body)}{sect}</w:body></w:document>'


def write_docx(markdown_path: Path, output_path: Path, title: str) -> None:
    document_xml = build_doc(markdown_path.read_text(encoding="utf-8"), title)
    header_xml = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:hdr xmlns:w="{NS_W}" xmlns:r="{NS_R}">{para(title, style="Normal", color="64748B", size=18, jc="right", after=0)}</w:hdr>'
    footer_xml = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr xmlns:w="{NS_W}" xmlns:r="{NS_R}"><w:p><w:pPr><w:jc w:val="center"/></w:pPr>{run("Page ", color="64748B", size=18)}<w:fldSimple w:instr="PAGE"><w:r><w:rPr><w:color w:val="64748B"/><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple>{run(" / ", color="64748B", size=18)}<w:fldSimple w:instr="NUMPAGES"><w:r><w:rPr><w:color w:val="64748B"/><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple></w:p></w:ftr>'

    for xml in (document_xml, header_xml, footer_xml, styles_xml()):
        ET.fromstring(xml)

    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
  <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>
  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
</Types>"""
    root_rels = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{NS_REL}"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'
    doc_rels = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{NS_REL}"><Relationship Id="rIdHeader" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/><Relationship Id="rIdFooter" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>'
    settings = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:settings xmlns:w="{NS_W}"><w:defaultTabStop w:val="420"/></w:settings>'

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("word/document.xml", document_xml)
        zf.writestr("word/_rels/document.xml.rels", doc_rels)
        zf.writestr("word/styles.xml", styles_xml())
        zf.writestr("word/settings.xml", settings)
        zf.writestr("word/header1.xml", header_xml)
        zf.writestr("word/footer1.xml", footer_xml)

    with ZipFile(output_path) as zf:
        bad = zf.testzip()
        if bad:
            raise RuntimeError(f"Invalid DOCX zip member: {bad}")
        ET.fromstring(zf.read("word/document.xml").decode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a defense-guide Markdown file to styled DOCX.")
    parser.add_argument("--input", required=True, type=Path, help="Input Markdown file")
    parser.add_argument("--output", required=True, type=Path, help="Output DOCX file")
    parser.add_argument("--title", default="Thesis Defense Q&A Guide", help="Cover/header title")
    args = parser.parse_args()
    write_docx(args.input, args.output, args.title)
    print(args.output.resolve())
    print(args.output.stat().st_size)


if __name__ == "__main__":
    main()
