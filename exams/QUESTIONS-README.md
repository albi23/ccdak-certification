# CCDAK Quiz — Exam Builder

## 1. What this project contains

- **Exam folder** — any sub-directory of `exams/` that contains files named
  `exam-questions-<N>.md`. Each such `.md` file becomes one "Exam" in the quiz.
- **Generated HTML** — `exam-test-aggregate.html`. **Never edit it by hand**; it is
  overwritten on every build. Edit the Markdown or `quiz-template.html` instead.

<img src="./img/img.png" alt="Kafka SSL FLOW">

### The quiz app features (from `quiz-template.html`)
- Per-exam timer (counts elapsed time); **Pause** button.
- Navigation between exams and between questions; an answer-review grid.
- Grading: correct / incorrect / unattempted, with a final time and score %.
- **Pass threshold = 70%**, computed as `correct / in-scope questions`
  (🚫 out-of-scope questions are excluded from scoring).
- State persisted in `localStorage` under the key `ccdak_quiz_<folder>`
  (the combined build uses `folder = "all"` → `ccdak_quiz_all`).
- Answer-review grid cell colors: **green = correct, red = incorrect,
  yellow = unattempted**; out-of-scope cells get a dashed border + 🚫 marker.

---

## 2. How to build

From inside the `exams/` directory:

```bash
./build.sh                                  # DEFAULT: one combined HTML for ALL folders
./build.sh --single-output                  # same as default (explicit)
./build.sh --single-output 1.medium 2.harder # combine only these folders
./build.sh --per-folder                     # one HTML per folder (written into each folder)
./build.sh 1.medium                         # per-folder build of just 1.medium
```

- **Default (combined)** writes one `exam-test-aggregate.html` into `exams/`,
  embedding every exam from every folder. Exam ids are `<folder>--exam-<N>` and
  names are `<label> · Exam <N>` (e.g. `medium · Exam 7`).
- **Per-folder** writes one `exam-test-aggregate.html` inside each folder,
  embedding only that folder's exams.

Requirements: **Python 3** only (no packages). On Windows use WSL or Git Bash,
or run `python3 build.py` directly.

The build prints one line per exam with its question count and a `!! N questions
missing an answer` warning if any `**Answer:**` line is missing.

---

## 3. Markdown question format (the contract)

Every question is parsed from a block that starts at a `## ... Question N ...` header
and runs until the next such header. The exact rules the parser enforces:

### 3.1 Header
```
## Question 1 (Category):
## 🚫 Question 1 (Category):      # 🚫 marks a question OUT of CCDAK scope
```
- Pattern: `## [🚫 ]Question <number>[ (Category)][:]`
- The `🚫` flag (optional) excludes the question from scoring and shows an
  out-of-scope badge/marker.
- `(Category)` is optional but recommended. Use the project's category vocabulary:
  *Kafka Core Concepts, Kafka Producers, Kafka Consumers, Kafka Internals,
  Reliable Data Delivery, Stream Processing, Kafka Connect,
  Programming & Serialization, Kafka Ecosystem, Kafka Setup and Operations.*

### 3.2 Question stem
Everything between the header and the **first option line** is the stem.
- Plain prose lines are collapsed into a single paragraph (line breaks joined with spaces).
- A fenced code block (```` ``` ````) in the stem is preserved verbatim and rendered
  as a code box.

### 3.3 Options
```
- A. First option text
- B. Second option text
...
- F. Up to F
```
- Pattern: `- <LETTER>. <text>` where `<LETTER>` is `A`–`F`.
- Options must be **contiguous** (no blank lines or other text between them);
  the parser stops at the first non-option line.

### 3.4 Instruction / select-N line
```
Choose the correct answer.
Choose the correct answers (select 3).
```
- The words `two | three | four | 2 | 3 | 4 | all` after `select` set the
  multi-select count. Any `select`-line (or 2+ answers below) marks the question
  as multi-select.

### 3.5 Answer + explanation block
```
<details>
<summary>Response:</summary>

**Answer:** C, D, E, F

**Explanation:**

Free-form explanation text...

Source: ...

**Detailed explanation of each option:**

1. ✅ **A. ...**
   **Correct**. ...
2. ❌ **B. ...**
   **Incorrect**. ...

</details>
```
- `**Answer:**` — a comma/space separated list of letters `A`–`F`.
  This is required; without it the build warns and the question can't be scored.
- The **explanation shown in the HTML** is *everything* from after
  `**Explanation:**` up to the closing `</details>` — including the
  `**Detailed explanation of each option:**` section. So put anything you want the
  learner to see inside `<details>`, after `**Explanation:**`.

### 3.6 Ordering (drag-and-drop) questions

An **ordering** question asks the learner to put the options into the correct
**sequence** (e.g. the steps of the consumer poll loop, or a transactional
producer's calls). In the UI the options become a reorderable list the learner
can **drag**, or move with ▲▼ buttons; it is graded **order-sensitively**.

It uses the same block structure as a normal question, with two differences:

1. The **instruction line** must trigger ordering mode. The parser switches to an
   ordering question when that line (the text between the options and `<details>`)
   contains any of: **`arrange`**, **`in the correct order`**, **`into the correct
   order`**, **`correct order`**, or **`correct sequence`** (case-insensitive).
   Recommended: `Arrange the steps in the correct order.`
2. `**Answer:**` lists **every** option letter **in the correct order** — this is
   the sequence, not an unordered set. Order matters: `C, A, B, D` ≠ `A, B, C, D`.

List the options in any order you like in the Markdown (they are shown in that
initial order and the learner rearranges them). Example:

```markdown
## Question 35 (Kafka Consumers):
Arrange the following steps of a Kafka consumer's lifecycle into the correct order.

- A. `poll()` the broker to fetch a batch of records
- B. Process the records returned by the poll
- C. `subscribe()` to one or more topics
- D. Commit the offsets of the processed records

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** C, A, B, D

**Explanation:**

Subscribe once, then loop: poll → process → commit.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 (The Poll Loop)

**Detailed explanation of each option:**

- **C. `subscribe()` to one or more topics** — Step 1: join the group.
- **A. `poll()` the broker to fetch a batch of records** — Step 2: fetch records.
- **B. Process the records returned by the poll** — Step 3: application logic.
- **D. Commit the offsets of the processed records** — Step 4: record progress.

</details>
```

Notes:
- Do **not** add a `select N` line to an ordering question — `select` would make it
  a checkbox multi-select instead. The ordering instruction line replaces it.
- An ordering question is **correct only if the full sequence matches** `**Answer:**`.
  Until the learner moves at least one item, the question counts as *unattempted*.
- For the per-option breakdown, a plain bullet list (as above) reads well since
  there is no single "correct subset"; any content inside `<details>` still shows.

---

## 4. How characters / styles are escaped, rendered, and translated

The builder is careful to **escape HTML first, then apply a small, fixed set of
Markdown rules**. This keeps the output safe (no raw HTML injection from question
text) while still rendering the formatting you want.


### 4.1 Inline formatting (stems, options, explanations)
After escaping, this light Markdown is translated:

| You write           | Renders as                     | Where it works                 |
|---------------------|--------------------------------|--------------------------------|
| `` `code` ``        | inline `<code>` (grey pill)    | stems, options, explanations   |
| `**bold**`          | **bold** (`<strong>`)          | stems, options, explanations   |
| newline (in explanation) | line break (`<br>`)       | explanations only              |

- Inline **backticks** → a styled inline-code span. Example:
  `` Enable `max.poll.interval.ms` `` renders the config name as code.
- The content *inside* backticks is still HTML-escaped, so `` `a<b>` `` is safe.
- Backticks must be **paired on the same logical line**; an unmatched `` ` `` is
  left as a literal backtick.

### 4.2 Block code (stems only)
A fenced block in the stem:
<pre>
```
some code
spanning lines
```
</pre>
is rendered as a `&lt;pre&gt;&lt;code&gt;` box: newlines and spacing are preserved,
and no inline Markdown is applied inside it (it is code, shown verbatim but escaped).

### 4.4 What is NOT translated
To keep parsing predictable, the builder does **not** implement full Markdown. The
following are shown literally (after HTML-escaping): headings `#`, lists `-`/`1.`,
links `[text](url)`, italics `*x*` / `_x_`, blockquotes `>`, tables, and images.
If you need emphasis use `**bold**`; if you need monospace use `` `backticks` ``.

> Note: `*single asterisks*` are **not** italic — only `**double**` is bold.
> Avoid stray single `*` in option text so it isn't confused with bold markers.

---

## 5. Adding new questions without breaking the parser

1. **Pick the file.** Add to an existing `exam-questions-<N>.md`, or create a new
   `exam-questions-<N>.md` in an exam folder (it becomes a new "Exam N").
   The file's number `<N>` only sets ordering/label; it need not be contiguous.

2. **Copy the exact skeleton** below and fill it in:

```markdown
## Question 30 (Stream Processing):
Short stem text. You can use `inline code` and **bold**.

- A. First choice (may use `code`/**bold**)
- B. Second choice
- C. Third choice
- D. Fourth choice

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C
 
**Explanation:**

Why C is correct and the others are not.

Source: Kafka: The Definitive Guide 2nd ed. Ch. X; https://kafka.apache.org/documentation/

**Detailed explanation of each option:**

1. ❌ **A. First choice**
   **Incorrect**. Reason.
2. ❌ **B. Second choice**
   **Incorrect**. Reason.
3. ✅ **C. Third choice**
   **Correct**. Reason.
4. ❌ **D. Fourth choice**
   **Incorrect**. Reason.

</details>
```

   For a multi-select question, use `**Answer:** C, D, E` and an instruction line
   like `Choose the correct answers (select 3).`.
   For an **ordering (drag-and-drop)** question, use an instruction line like
   `Arrange the steps in the correct order.` and list **all** letters in sequence
   in `**Answer:**` (see §3.6). Do **not** add a `select N` line to it.
   For an out-of-scope question, prefix the header: `## 🚫 Question 30 (...):`.

3. **Rebuild and verify:**
   ```bash
   ./build.sh
   ```
   Check the console output: each file should show the expected question count and
   **no** `!! N questions missing an answer` warning. Open
   `exam-test-aggregate.html` to confirm formatting.

---

## 4. Quick reference

| Element            | Markdown                                   | Result in HTML                         |
|--------------------|--------------------------------------------|----------------------------------------|
| Question header    | `## Question 5 (Kafka Consumers):`         | new question, category badge           |
| Out-of-scope       | `## 🚫 Question 5 (...):`                   | excluded from score, 🚫 badge/marker    |
| Option             | `- A. text`                                | selectable choice A                    |
| Single answer      | `Choose the correct answer.`               | radio buttons                          |
| Multi answer       | `Choose the correct answers (select 3).`   | checkboxes, requires 3                 |
| Ordering (drag)    | `Arrange the steps in the correct order.`  | reorderable list, drag / ▲▼, order-graded |
| Correct answer(s)  | `**Answer:** B, D`                          | grading key                            |
| Correct order      | `**Answer:** C, A, B, D` (all, in sequence) | expected order for an ordering question |
| Inline code        | `` `group.id` ``                            | `group.id` (inline code pill)          |
| Bold               | `**important**`                             | **important**                          |
| Code block         | ```` ```\n...\n``` ````                     | preformatted code box                  |
| Explanation        | text after `**Explanation:**` … `</details>`| shown under the question after grading |
