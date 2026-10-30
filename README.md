# gpt-resolve

**Can AI solve Brazil's hardest university entrance exams?** gpt-resolve turns an exam PDF into a ready-to-print PDF of model solutions, written like a cursinho answer sheet: step by step, in standardized LaTeX, each one reviewed by an adversarial AI judge and, optionally, graded against an answer key.

```bash
gpt-resolve resolve -p "IME 2027 Matematica.pdf" -t "IME 2027 - Matemática"
# -> IME 2027 Matematica_solutions/claude_opus_5_5/solutions_compiled.pdf
```

## Results

Score is the share of items that match the answer key (or where the key was found wrong). ITA 2025 scores were reviewed by hand.

| Exam     | Section   | Solver            | Judge scores | Score | Solutions | Grade report | Report |
| -------- | --------- | ----------------- | ------------ | ----- | --------- | ------------ | ------ |
| ITA 2027 | Math      | `claude-opus-5-5` | 9.5 – 10     | **100%** (12/12) | [PDF](exams/ita_2027/math/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/ita_2027/math/essays/solutions/claude_opus_5_5/grade_report.pdf) | [ITA 2027](exams/ita_2027/report.md) |
| ITA 2027 | Chemistry | `claude-opus-5-5` | 9.0 – 9.5    | **99%** (36/37)  | [PDF](exams/ita_2027/chemistry/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/ita_2027/chemistry/essays/solutions/claude_opus_5_5/grade_report.pdf) | [ITA 2027](exams/ita_2027/report.md) |
| ITA 2027 | Physics   | `claude-opus-5-5` | 9.0 – 9.5    | **100%** (24/24) | [PDF](exams/ita_2027/physics/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/ita_2027/physics/essays/solutions/claude_opus_5_5/grade_report.pdf) | [ITA 2027](exams/ita_2027/report.md) |
| IME 2027 | Math      | `claude-opus-5-5` | 9.5          | **100%** (12/12) | [PDF](exams/ime_2027/math/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/ime_2027/math/essays/solutions/claude_opus_5_5/grade_report.pdf) | [IME 2027](exams/ime_2027/report.md) |
| IME 2027 | Physics   | `claude-opus-5-5` | 9.0 – 9.5    | **100%** (30/30) | [PDF](exams/ime_2027/physics/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/ime_2027/physics/essays/solutions/claude_opus_5_5/grade_report.pdf) | [IME 2027](exams/ime_2027/report.md) |
| IME 2027 | Chemistry | `claude-opus-5-5` | 9.0 – 9.5    | **100%** (25/25) | [PDF](exams/ime_2027/chemistry/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/ime_2027/chemistry/essays/solutions/claude_opus_5_5/grade_report.pdf) | [IME 2027](exams/ime_2027/report.md) |
| Unicamp 2027 | 1st phase (all subjects) | `claude-opus-5-5` | 9.0 – 10 | **100%** (72/72) | [PDF](exams/unicamp_2027/first_phase/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/unicamp_2027/first_phase/solutions/claude_opus_5_5/grade_report.pdf) | [Unicamp 2027](exams/unicamp_2027/report.md) |
| Escola Naval 2026 | Math | `claude-opus-5-5` | 9.0 – 9.5 | **100%** (22/22) | [PDF](exams/escola_naval_2026/math/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/escola_naval_2026/math/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) | [Escola Naval 2026](exams/escola_naval_2026/report.md) |
| Escola Naval 2026 | Physics | `claude-opus-5-5` | 9.0 – 9.5 | **95%** (21/22) | [PDF](exams/escola_naval_2026/physics/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/escola_naval_2026/physics/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) | [Escola Naval 2026](exams/escola_naval_2026/report.md) |
| AFA 2027 | Math | `claude-opus-5-5` | 9.0 – 9.5 | **94%** (15/16) | [PDF](exams/afa_2027/math/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/afa_2027/math/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) | [AFA 2027](exams/afa_2027/report.md) |
| AFA 2027 | Physics | `claude-opus-5-5` | 9.0 – 9.5 | **100%** (16/16) | [PDF](exams/afa_2027/physics/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](exams/afa_2027/physics/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) | [AFA 2027](exams/afa_2027/report.md) |
| ITA 2025 | Math      | `o3` / `o4-mini`  | –            | 98%   | [o3](exams/ita_2025/math/essays/solutions/o3/solutions_compiled.pdf) · [o4-mini](exams/ita_2025/math/essays/solutions/o4_mini/solutions_compiled.pdf) | – | [ITA 2025](exams/ita_2025/report.md) |
| ITA 2025 | Math      | `o1` / `o1-preview` | –          | 95% / 90% | [o1](exams/ita_2025/math/essays/solutions/o1/solutions_compiled.pdf) · [o1-preview](exams/ita_2025/math/essays/solutions/o1_preview/solutions_compiled.pdf) | – | [ITA 2025](exams/ita_2025/report.md) |
| ITA 2025 | Chemistry | `o1-preview`      | –            | 95%   | [PDF](exams/ita_2025/chemistry/essays/solutions/solutions_compiled.pdf) | – | [ITA 2025](exams/ita_2025/report.md) |
| ITA 2025 | Physics   | `o1-preview`      | –            | 65%   | [PDF](exams/ita_2025/physics/essays/solutions/solutions_compiled.pdf) | – | [ITA 2025](exams/ita_2025/report.md) |

Each 2027 essay exam (10 questions) took under 7 minutes end to end. Escola Naval and AFA are multiple choice (Math and Physics only), graded against the official keys; in the one mismatch per exam the grader found the key wrong (Escola Naval Physics Q34) or the statement ambiguous (AFA Math Q22). The Unicamp 1st phase (72 questions of every subject, humanities included) took 19 minutes and matched the official key on all 72. Next on the list: Fuvest/USP and ENEM.

## How it works

| Step | What happens | Output |
| ---- | ------------ | ------ |
| 1. Extract | An agent reads the exam PDF and lists each question (number, pages, transcription). Cached, so re-runs skip it. | `questions.json` |
| 2. Solve | One agent per question (in parallel) reads the original pages and figures and may check its math with Python. | `q<n>_solution.txt` |
| 3. Judge | An adversarial agent first solves the question **blind**, then scores the whole resolution from 0 to 10 (correctness, completeness, rigor, clarity). Below the pass score, the solver revises with the critique. Optional (`--no-judge`). | `q<n>_judge.json` |
| 4. Compile | All solutions go into one PDF, plus an appendix with each judge score and review. | `solutions_compiled.pdf` |
| 5. Grade | Optional, separate command: compares the solutions with an answer key you provide. | `grade_report.pdf` |

Agents are sandboxed: they can only read the exam files and their own work folder, and Bash is limited to local computation (no network), so an answer key on your machine can't leak into a solution.

## Why it's different

| | |
| - | - |
| **Standardized LaTeX** | Every solution is a single `\section*` in plain LaTeX (only `amsmath`, `amssymb`, `amsfonts`, `graphicx`, `tikz`, `pgfplots`), no Unicode inside formulas, decimal comma, no nested display math. All exams compile with the same preamble into the same layout, and a solution with broken LaTeX becomes a placeholder instead of breaking the PDF. |
| **Exam-grade prompts** | The solver writes like a cursinho model answer: correct, complete, rigorous and didactic, about one page per question, ending with the final answer. All prompts and output schemas live in [`prompts.py`](src/gpt_resolve/prompts.py), in Portuguese. |
| **A judge that isn't anchored** | The judge solves the question before seeing the candidate, lists the pitfalls, and only then reviews it. Disagreements are resolved, not copied. |
| **Answer key stays out** | Solver and judge never see an answer key. Grading is a separate step, run after the solutions are done. |
| **Swappable backend** | Runs on the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview). Other backends plug in as providers in [`providers/`](src/gpt_resolve/providers/). |

## Quick start

Requirements: Python 3.10+, the [`claude` CLI](https://docs.claude.com/en/docs/claude-code) logged in (`claude login` for a Claude subscription, or `ANTHROPIC_API_KEY`), and a LaTeX distribution with `pdflatex` for the PDFs ([TeX Live](https://www.tug.org/texlive/), [MacTeX](https://www.tug.org/mactex/) or TinyTeX).

```bash
git clone https://github.com/lgabs/gpt-resolve && cd gpt-resolve
pip install -e .
claude login
gpt-resolve resolve -p exam.pdf -q 1,2 -t "My exam"     # solve questions 1 and 2
```

## Commands

| Command | Use it to |
| ------- | --------- |
| `gpt-resolve resolve` | Solve an exam (PDF, or a folder with `q1.jpg`, `q2.jpg`, ... and optional `conventions.jpg`) |
| `gpt-resolve grade` | Compare solutions with an answer key |
| `gpt-resolve compile-solutions` | Rebuild the PDF from existing `q<n>_solution.txt` files |

Run any of them with `--help` for all options.

### `resolve`

| Option | Default | Description |
| ------ | ------- | ----------- |
| `-p, --path` | – | Exam PDF or image folder |
| `-q, --questions` | all | Questions to solve, e.g. `1,3,5` |
| `-o, --output` | `<pdf name>_solutions/<model>/` | Output folder |
| `-t, --title` | `Soluções` | Title of the compiled PDF |
| `-m, --model` | `claude-opus-5-5` | Solver model |
| `--judge / --no-judge` | `--judge` | Review with the adversarial judge. `--no-judge` runs one solver pass per question (faster, cheaper, no score) |
| `--judge-model` | `claude-opus-5-5` | Judge model |
| `--pass-score` | `9` | Minimum judge score (0–10) to approve |
| `--max-rounds` | `3` | Max solve/judge rounds per question; the best attempt is kept |
| `--effort` | `xhigh` | Reasoning effort: `low`, `medium`, `high`, `xhigh`, `max` |
| `--concurrency` | `4` | Questions solved in parallel |
| `--compile / --no-compile` | `--compile` | Compile the PDF at the end |
| `--quiet` | off | Hide each agent's tool calls |
| `--dry-run` | off | Offline mock agent, to test the pipeline |

A failing agent is retried, and a question that still fails doesn't stop the others: re-run it with `-q <n>`.

### Compare with an answer key (`grade`)

```bash
gpt-resolve grade -p exams/ime_2027/physics/essays/solutions/claude_opus_5_5 \
  -k answer_key.json -e exams/ime_2027/physics/essays/exam.pdf
```

One grader agent per question compares the final answers item by item, redoes the work where they disagree (keys can be wrong too) and lists the doubts worth checking with a teacher. A question's score is the share of its items where the solution is right.

**You bring the answer key.** gpt-resolve doesn't fetch or build answer keys: getting one (official or from a cursinho) and organizing it in the format below is up to you. Any tool works for that, including an LLM, but it is outside this project.

```json
{
  "source": "Name of the answer key",
  "questions": [
    {"number": 1, "answer": {"a": "v0 = 250 m/s", "b": "T = 4000 K"}, "resolution": "optional worked solution", "url": "optional link"}
  ]
}
```

| Field | Required | Description |
| ----- | -------- | ----------- |
| `source` | no | Shown in the report |
| `number` | yes | Question number, as in the exam |
| `answer` | yes | A string, or an object with one answer per item |
| `resolution` | no | The key's worked solution; helps the grader judge disagreements |
| `url` | no | Link to the original key |

Outputs go to the solutions folder: `q<n>_grade.json` (per item: both answers, verdict, who is right and why), `grade_report.md` and `grade_report.pdf`. Options: `-q`, `-m`, `--effort`, `--concurrency`, `--no-compile`, `-t`, `--dry-run`.

### `compile-solutions`

```bash
gpt-resolve compile-solutions -p exam_solutions_folder -t "Your exam title" -a "Author"
```

## Costs

With a Claude subscription, runs count against your plan's usage limits. With `ANTHROPIC_API_KEY` you pay per token:

| Mode | Agent sessions per question |
| ---- | --------------------------- |
| `--no-judge` | 1 (solver) |
| With judge, approved in round 1 | 3 (blind judge, solver, review) |
| Each extra round | +2 (solver, review) |

Plus one extraction per PDF and, for `grade`, one session per question. Lower `--effort`, `--max-rounds` or `--concurrency` to spend less.

`resolve` and `grade` log each agent's estimated cost (API prices, as reported by the SDK) and the total at the end. For reference, at `--effort xhigh` the Escola Naval 2026 and AFA 2027 Math and Physics exams (76 multiple-choice questions) cost about US$ 0.50 per question to solve and US$ 0.10 to grade.

## Changelog

| Version | Changes |
| ------- | ------- |
| v0.6 | New `grade` command. `--no-judge` option. No breaking changes. |
| v0.5 | **Breaking:** OpenAI replaced by the Claude Agent SDK (`OPENAI_API_KEY` ignored, needs the `claude` CLI). Python 3.10+. `-p` accepts PDFs. `--max-tokens-output` replaced by `--effort`; new judge options. Outputs go to `<pdf name>_solutions/<model>/`. |
| ≤ v0.4 | OpenAI pipeline (`o1-preview`, `o1`, `o3`, `o4-mini`), one image per question. |

## Contributing

Ideas and PRs are welcome: new exams, better prompts, new providers, docs. Fork, branch, and open a PR with a clear description and, for new exam solutions, the results table updated. For bigger changes, open an issue first.
