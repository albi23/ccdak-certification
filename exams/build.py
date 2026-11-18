#!/usr/bin/env python3
"""
Build a self-contained quiz HTML from the markdown exams.

Usage:
    python3 build.py                     # DEFAULT: one combined HTML for ALL folders
    python3 build.py --single-output     # same as default (explicit)
    python3 build.py --single-output 1.medium 2.harder   # combine only these
    python3 build.py --per-folder        # one HTML per folder (into each folder)
    python3 build.py --all               # alias of --per-folder
    python3 build.py 1.medium            # per-folder build of just 1.medium

Default (--single-output): walks every exam folder (e.g. "1.medium",
"2.harder"), merges all their `exam-questions-*.md` exams, and writes a
single `exam-test-aggregate.html` into the `exams/` directory.

Per-folder mode writes one `exam-test-aggregate.html` inside each folder,
embedding only that folder's exams. All outputs work offline with no server.
"""
import re
import os
import sys
import json
import glob
import gzip
import base64

HERE = os.path.dirname(os.path.abspath(__file__))

# ----- markdown header for a question -----
# Matches:  "## Question 1:"  and  "## 🚫 Question 1 (Category):"
HEADER_RE = re.compile(r'^##\s+(?P<flag>🚫\s*)?Question\s+(?P<num>\d+)\s*(?:\((?P<cat>[^)]*)\))?\s*:?', re.U)
OPT_RE = re.compile(r'^- ([A-F])\.\s+(.*)$')


def parse_file(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    idxs = [i for i, l in enumerate(lines) if HEADER_RE.match(l)]
    questions = []
    for k, i in enumerate(idxs):
        end = idxs[k + 1] if k + 1 < len(idxs) else len(lines)
        q = parse_block(lines[i:end])
        if q and q['options']:
            questions.append(q)
    return questions


def esc_html(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def inline_md(s):
    """Escape HTML, then render inline `code` spans and **bold**."""
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '`':
            end = s.find('`', i + 1)
            if end != -1:
                out.append('<code>' + esc_html(s[i + 1:end]) + '</code>')
                i = end + 1
                continue
        out.append(esc_html(c))
        i += 1
    html = ''.join(out)
    # bold on already-escaped text (markers have no HTML-special chars)
    import re as _re
    html = _re.sub(r'\*\*([^*]+?)\*\*', r'<strong>\1</strong>', html)
    return html



def build_stem(raw_lines):
    """Return (plain_text, html) for a question stem, preserving ``` code blocks.

    Prose lines are collapsed with spaces; fenced code blocks keep their
    newlines and are wrapped in <pre><code>.
    """
    plain_parts = []
    html_parts = []
    prose = []          # pending prose lines
    code = None         # pending code lines (inside a fence) or None

    def flush_prose():
        if prose:
            text = ' '.join(p.strip() for p in prose if p.strip()).strip()
            if text:
                plain_parts.append(text)
                html_parts.append('<p>' + inline_md(text) + '</p>')
            prose.clear()

    for line in raw_lines:
        if line.strip().startswith('```'):
            if code is None:
                flush_prose()
                code = []
            else:
                body = '\n'.join(code).rstrip('\n')
                plain_parts.append(body)
                html_parts.append('<pre><code>' + esc_html(body) + '</code></pre>')
                code = None
            continue
        if code is not None:
            code.append(line)
        else:
            prose.append(line)

    if code is not None:  # unterminated fence: treat as code
        body = '\n'.join(code).rstrip('\n')
        plain_parts.append(body)
        html_parts.append('<pre><code>' + esc_html(body) + '</code></pre>')
    flush_prose()

    return ' '.join(plain_parts).strip(), ''.join(html_parts)


def parse_block(block):
    header = block[0]
    hm = HEADER_RE.match(header)
    category = (hm.group('cat') or '').strip() if hm else ''
    out_of_scope = bool(hm and hm.group('flag'))

    text = '\n'.join(block)

    # locate first option line
    first_opt = None
    for j, l in enumerate(block[1:], 1):
        if OPT_RE.match(l):
            first_opt = j
            break
    if first_opt is None:
        return None

    # question text = lines between header and first option.
    # Preserve fenced ``` code blocks; collapse prose into single lines.
    raw_qlines = block[1:first_opt]
    qtext, qhtml = build_stem(raw_qlines)

    # contiguous options
    options = []
    j = first_opt
    while j < len(block):
        m = OPT_RE.match(block[j])
        if not m:
            break
        options.append({'letter': m.group(1), 'text': m.group(2).strip()})
        j += 1

    # Only the instruction line(s) between the options and <details> should
    # decide question type, so explanation prose (e.g. a note mentioning
    # "select 2") can't accidentally trigger multi-select or ordering.
    instr_lines = []
    for l in block[j:]:
        if l.strip().startswith('<details'):
            break
        instr_lines.append(l)
    instr_line = ' '.join(instr_lines).lower()

    # multi / select-N detection from the instruction line
    sel_n = None
    multi = False
    ms = re.search(r'select\s+(two|three|four|2|3|4|all)', instr_line)
    if ms:
        word = ms.group(1)
        sel_n = {'two': 2, 'three': 3, 'four': 4}.get(word)
        if word in ('2', '3', '4'):
            sel_n = int(word)
        multi = True

    # ordering/sequence question: the instruction asks to arrange/order the
    # options into a sequence. Here **Answer:** lists ALL letters in the
    # correct order, and the answer is graded order-sensitively.
    ordering = bool(re.search(
        r'arrange|in(to)?\s+the\s+correct\s+order|correct\s+order|correct\s+sequence',
        instr_line))

    # answer letters
    answers = []
    am = re.search(r'^\*\*Answer:\*\*\s*(.+)$', text, re.M)
    if am:
        answers = [a for a in re.split(r'[,\s]+', am.group(1).strip()) if re.match(r'^[A-F]$', a)]
    if ordering:
        # ordering questions are neither single- nor multi-select buttons
        multi = False
        sel_n = len(answers)
    elif len(answers) > 1:
        multi = True

    # Capture the FULL explanation: everything from after **Explanation:**
    # up to the closing </details>, including the per-option
    # "Detailed explanation of each option" block.
    explanation = ''
    em = re.search(r'\*\*Explanation:\*\*\s*(.*?)</details>', text, re.S)
    if em:
        explanation = em.group(1).strip()
        if explanation == '(No explanation provided in source.)':
            explanation = ''
        # Drop a lone "see below" pointer when a detailed block follows.
        explanation = re.sub(
            r'^\(See per-option explanations below\.\)\s*',
            '', explanation).strip()

    return {
        'q': qtext,
        'qHtml': qhtml,
        'category': category,
        'outOfScope': out_of_scope,
        'options': options,
        'answers': answers,
        'multi': multi,
        'ordering': ordering,
        'selectN': sel_n if sel_n else (len(answers) if len(answers) > 1 else 1),
        'explanation': explanation,
    }


def build_data(folder_path, folder_name):
    paths = glob.glob(os.path.join(folder_path, 'exam-questions-*.md'))
    paths.sort(key=lambda p: int(re.search(r'-(\d+)\.md$', p).group(1)))
    exams = []
    for p in paths:
        num = int(re.search(r'-(\d+)\.md$', p).group(1))
        qs = parse_file(p)
        exams.append({
            'id': f'exam-{num}',
            'name': f'Exam {num}',
            'file': os.path.basename(p),
            'questions': qs,
        })
    return {'folder': folder_name, 'exams': exams}


def folder_label(folder_name):
    """Human label for a folder, e.g. "1.medium" -> "medium"."""
    return re.sub(r'^\d+\.', '', folder_name) or folder_name


def build_combined_data(folder_paths):
    """Merge exams from several folders into one dataset.

    Exam ids/names are prefixed with their folder so they stay unique and
    distinguishable in the combined quiz.
    """
    exams = []
    for fp in folder_paths:
        fp = os.path.abspath(fp)
        fname = os.path.basename(fp.rstrip(os.sep))
        label = folder_label(fname)
        data = build_data(fp, fname)
        for e in data['exams']:
            exams.append({
                'id': f'{fname}--{e["id"]}',
                'name': f'{label} · {e["name"]}',
                'file': f'{fname}/{e["file"]}',
                'questions': e['questions'],
            })
    return {'folder': 'all', 'exams': exams}


def render_html(data):
    template = open(os.path.join(HERE, 'quiz-template.html'), encoding='utf-8').read()
    data_json = json.dumps(data, ensure_ascii=False)
    # gzip-compress the UTF-8 JSON and base64-encode it so it can be embedded
    # as a plain JS string literal. The browser decompresses it natively via
    # DecompressionStream('gzip') at load time.
    gz = gzip.compress(data_json.encode('utf-8'), compresslevel=9)
    data_b64 = base64.b64encode(gz).decode('ascii')
    data_literal = json.dumps(data_b64)  # safe JS string literal
    return (template
            .replace('__DATA_JSON__', data_literal)
            .replace('__FOLDER__', data['folder']))


def build_folder(folder_path):
    folder_path = os.path.abspath(folder_path)
    folder_name = os.path.basename(folder_path.rstrip(os.sep))
    data = build_data(folder_path, folder_name)
    total = sum(len(e['questions']) for e in data['exams'])
    if not data['exams']:
        print(f"  [skip] {folder_name}: no exam-questions-*.md files found")
        return
    html = render_html(data)
    out = os.path.join(folder_path, 'exam-test-aggregate.html')
    open(out, 'w', encoding='utf-8').write(html)
    print(f"  [ok]  {folder_name}: {len(data['exams'])} exams, {total} questions -> {out}")
    for e in data['exams']:
        missing = sum(1 for q in e['questions'] if not q['answers'])
        warn = f"  !! {missing} questions missing an answer" if missing else ""
        print(f"         {e['file']}: {len(e['questions'])} q{warn}")


def build_single_output(folder_paths):
    """Build ONE combined html (all folders) into the exams/ dir."""
    folder_paths = [os.path.abspath(p) for p in folder_paths]
    data = build_combined_data(folder_paths)
    if not data['exams']:
        print("  [skip] no exam-questions-*.md files found in any folder")
        return
    total = sum(len(e['questions']) for e in data['exams'])
    html = render_html(data)
    out = os.path.join(HERE, 'exam-test-aggregate.html')
    open(out, 'w', encoding='utf-8').write(html)
    print(f"  [ok]  combined: {len(data['exams'])} exams, {total} questions -> {out}")
    for e in data['exams']:
        missing = sum(1 for q in e['questions'] if not q['answers'])
        warn = f"  !! {missing} questions missing an answer" if missing else ""
        print(f"         {e['file']}: {len(e['questions'])} q{warn}")


def discover_folders():
    found = []
    for name in sorted(os.listdir(HERE)):
        p = os.path.join(HERE, name)
        if os.path.isdir(p) and glob.glob(os.path.join(p, 'exam-questions-*.md')):
            found.append(p)
    return found


def main(argv):
    args = argv[1:]

    single = False
    per_folder_all = False
    explicit = []
    for a in args:
        if a == '--single-output':
            single = True
        elif a in ('--per-folder', '--all'):
            per_folder_all = True
        elif a in ('-h', '--help'):
            print(__doc__)
            sys.exit(0)
        elif a.startswith('-'):
            print(f"  [skip] unknown option: {a}")
        else:
            explicit.append(a)

    def resolve(names):
        out = []
        for a in names:
            p = a if os.path.isabs(a) else os.path.join(HERE, a)
            if not os.path.isdir(p):
                print(f"  [skip] {a}: not a directory")
                continue
            out.append(p)
        return out

    # per-folder mode only when explicitly requested
    if per_folder_all or (explicit and not single):
        folders = resolve(explicit) if explicit else discover_folders()
        if not folders:
            print("No sub-folders with exam-questions-*.md found.")
            sys.exit(1)
        print("Building quizzes (per-folder)...")
        for f in folders:
            build_folder(f)
        print("Done.")
        return

    # default: single combined output across all (or the given) folders
    folders = resolve(explicit) if explicit else discover_folders()
    if not folders:
        print("No sub-folders with exam-questions-*.md found.")
        sys.exit(1)
    print("Building quiz (single combined output)...")
    build_single_output(folders)
    print("Done.")


if __name__ == '__main__':
    main(sys.argv)
