# gpt-resolve
Can GPT solve Brazilian university entrance exams?

This project is an implementation of how to use LLMs to solve challenging Brazilian university entrance exams.

We started with `o1-preview`, and `gpt-4o` to describe the exam images so that `o1-preview` could solve them, because it did not have image capabilities yet. Later versions passed images directly to `o1`, `o3` and `o4-mini`.

Since v0.5, the project runs on agents: the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview) reads the exam PDF, solves each question in its own agent, and an adversarial judge agent (which first solves the question blind) scores each resolution and asks for revisions until it is good enough. Results are saved as LaTeX files plus the judge reviews, and compiled into a PDF.

The project begins with the ITA (Instituto Tecnológico de Aeronáutica) 2025 exam, focusing first on the Math essay section. This section, from the recent exam on November 5, 2024, demands deep subject understanding and step-by-step solutions. More details are in the [report](exams/ita_2025/report.md) documentation.

**Spoilers: o1-preview scored 90% in the ITA 2025 Math Essay Exam, 95% in Chemistry Essay and only 65% in Physics Essay. o1 scored 95% in the same Math exam. On the IME 2027 Physics essay, Claude Opus 5.5 had all 10 questions approved by its judge (scores 9.0–9.5) in 6 minutes and matched the Poliedro answer key on all 30 items (100%, [report](exams/ime_2027/report.md)).**

After the first ITA 2025 exam is fully solved, the project will try to expand to other sections and eventually other exams. Feel free to contribute with ideas and implementations of other exams!

Table of some exams to be solved:

| Exam         | Year | Status        | Score | Report                             |
| ------------ | ---- | ------------- | ----- | ---------------------------------- |
| ITA          | 2025 | 🚧 In Progress | -     | [Report](exams/ita_2025/report.md) |
| IME          | 2027 | 🚧 In Progress | Physics: 100% | [Report](exams/ime_2027/report.md) |
| Escola Naval | 2025 | 📅 Todo        | -     | -                                  |
| Fuvest/USP   | 2025 | 📅 Todo        | -     | -                                  |
| AFA          | 2025 | 📅 Todo        | -     | -                                  |
| UNICAMP      | 2025 | 📅 Todo        | -     | -                                  |
| ENEM         | 2025 | 📅 Todo        | -     | -                                  |

# Breaking changes in v0.5

v0.5 replaces the OpenAI pipeline with the Claude Agent SDK. If you used v0.4:

- **Backend**: OpenAI is no longer used and `OPENAI_API_KEY` is ignored. You need the `claude` CLI ([Claude Code](https://docs.claude.com/en/docs/claude-code)) installed and logged in (`claude login` for a Claude subscription, or `ANTHROPIC_API_KEY`). New backends can be added as providers (`src/gpt_resolve/providers/`).
- **Python 3.10+** is required (Claude Agent SDK requirement).
- **Input**: `-p` now also accepts an exam PDF. The image folder layout still works, and `conventions.jpg` is now optional.
- **CLI options**: `--max-tokens-output` was removed; use `--effort`. `--model` now takes Claude model ids (default `claude-opus-5-5`). New: `--judge-model`, `--pass-score`, `--max-rounds`, `--concurrency`, `--provider`, `--quiet`, `-o/--output`, `--compile/--no-compile`, `-t/--title`.
- **Output**: for a PDF, solutions go to `<pdf name>_solutions/<model>/` by default. Each question also gets a `q<n>_judge.json`, and `resolve` compiles `solutions_compiled.pdf` at the end (with a judge appendix).
- **`compile-solutions`** no longer aborts on a solution with invalid LaTeX: it puts a placeholder in the PDF and prints a warning.
- **`--dry-run`** now uses an offline mock agent.

# Installation and How to use
gpt-resolve is distributed in pypi (v0.5 is installed from this repository until it is published):
```bash
pip install gpt-resolve
```

`gpt-resolve` provides a simple CLI with three main commands: `resolve` for solving exam questions, `grade` for comparing the solutions with an answer key, and `compile-solutions` for generating PDFs from the solutions, as you can check below. During development, install locally with `pip install -e .`.

### Solve exams with `resolve`

Since v0.5, `gpt-resolve` runs on the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), which drives the local `claude` CLI. That means it uses whatever auth your Claude Code has: your Claude subscription (after `claude login`) or `ANTHROPIC_API_KEY`.

How it works:
1. **Extract** (PDF only): an agent reads the exam PDF and lists the questions (number, pages, transcription). Cached in `questions.json`, so re-runs skip it.
2. **Solve**: each question runs in its own agent (default `claude-opus-5-5`), which can read the original pages/figures and use Python to check its work.
3. **Judge**: an adversarial agent (default `claude-opus-5-5`) solves the question independently and scores the *whole resolution* (correctness, completeness, rigor, clarity) from 0 to 10. Below `--pass-score` (default 9), the solver revises using the critique, up to `--max-rounds` (default 3). The best attempt is kept and flagged as approved or not.
   The judge works in two phases: it first solves the question blind (without seeing the candidate) and lists its pitfalls, then reviews the candidate against that reference, resolving any disagreement instead of anchoring on it.
4. **Compile**: a PDF with all solutions plus an appendix with each judge score and review (needs `pdflatex`).

```bash
claude login            # once, if using your subscription
pip install -e .
gpt-resolve resolve -p "IME 2027 Matematica.pdf" -q 1,2 -t "IME 2027 - Matemática"
```

Outputs go to `<pdf name>_solutions/<model>/`: `q<n>_solution.txt` (LaTeX), `q<n>_judge.json` (scores and reviews of every round) and `solutions_compiled.pdf`. The old layout of one image per question (`q1.jpg`, ..., optional `conventions.jpg`) still works by passing the folder to `-p`.

Agents are sandboxed by a `PreToolUse` hook: they can only read the exam files and their own work folder, and Bash is limited to local computation (no network, no files elsewhere), so answer keys on the machine can't leak in. The terminal shows each agent's tool calls and the judge scores live (`--quiet` hides tool calls); a failing agent is retried, and a question that still fails doesn't stop the others.

Useful options (see `gpt-resolve resolve --help`): `--model`, `--judge-model`, `--pass-score`, `--max-rounds`, `--effort`, `--concurrency`, `--no-compile`, `--dry-run` (offline mock).

Providers live in `src/gpt_resolve/providers/`: implement `Provider.run` and register it in `get_provider` to use another backend (`--provider`).


### Compare with an answer key with `grade`

Once a cursinho (or the official board) publishes its answer key, `grade` compares it with your solutions. Each question runs in its own grader agent (same Claude Agent SDK setup and sandbox as the solver, `--concurrency` in parallel), which compares the final answers item by item, redoes the work where they disagree (the key can be wrong too) and lists the points worth checking with a teacher.

```bash
gpt-resolve grade -p exams/ime_2027/physics/essays/solutions/claude_opus_5_5 \
  -k poliedro_key.json -e exams/ime_2027/physics/essays/exam.pdf
```

The answer key is a JSON file; `answer` is a string or an object with one answer per item, and `resolution` (the key's worked solution) is optional but helps the grader:

```json
{
  "source": "Poliedro",
  "questions": [
    {"number": 1, "answer": {"a": "v0 = 250 m/s", "b": "T = 4000 K"}, "resolution": "...", "url": "https://..."}
  ]
}
```

Outputs go to the solutions folder: `q<n>_grade.json` (per item: both answers, verdict, who is right and why; plus the doubts), `grade_report.md` and `grade_report.pdf` (LaTeX, compiled at the end unless `--no-compile`; scores, item verdicts and all doubts). The score of a question is the share of its items where the solution is right. The grader only sees the key through its prompt, and `-e` lets it read the exam pages listed in `questions.json`.

### Compile solutions with `compile-solutions`

Once you have the solutions in your exam folder `exam_path`, you can compile them into a single PDF running:
```bash
gpt-resolve compile-solutions -p exam_path --title "Your Exam Title --author 'o1 (OpenAI)'"
```

For that command to work, you'll need a LaTeX distribution in your system. See some guidelines [here](https://www.tug.org/texlive/) (MacTeX for MacOS was used to start this project). This project was developed with [MacTeX](https://www.tug.org/mactex/) distribution.

# Troubleshooting

Sometimes, it was observed that the output from `o1-preview` produced invalid LaTeX code when nesting display math environments (such as `\[...\]` and `\begin{align*} ... \end{align*}` together). The current prompt for `o1-preview` adds an instruction to avoid this, which works most of the time. If that happens, you can try to solve the question again by running `gpt-resolve resolve -p exam_path -q <question_number>`, or making more adjustments to the prompt, or fixing the output LaTeX code manually. Experiments with `o1` did not show any similar errors so far.

# Costs

With a Claude subscription, runs count against your plan's usage limits instead of being billed per token. With `ANTHROPIC_API_KEY`, each question costs at least three agent sessions (blind judge solution, solver, judge review), plus one solver + judge pair per revision round, and one extraction per PDF. Lower `--effort`, `--max-rounds` or `--concurrency` to spend less. For reference, the IME 2027 Physics essay (10 questions, all approved in the first round) ran in about 6 minutes at `--effort xhigh`.

Earlier OpenAI versions (v0.4 and before) were billed per token: for `o1` ($15/$60 per 1M input/output tokens), a 10-question exam with 10000 max tokens per question cost less than $6.

# Contributing

There are several ways you can contribute to this project:

- Add solutions for new exams or sections
- Improve existing solutions or model prompts
- Add automatic evaluation metrics for answers
- Create documentations for exams
- Report issues or suggest improvements

To contribute, simply fork the repository, create a new branch for your changes, and submit a pull request. Please ensure your PR includes:
- Clear description of the changes
- Updated table entry (if adding new exam solutions)
- Any relevant documentation

Feel free to open an issue first to discuss major changes or new ideas!

## Sponsors

<p align="center">
  <a href="https://www.buser.com.br">
    <img src="assets/sponsors/buser-logo.png" alt="Buser Logo" width="100"/>
  </a>
</p>

This project is proudly sponsored by [Buser](https://www.buser.com.br), Brazil's leading bus travel platform.
