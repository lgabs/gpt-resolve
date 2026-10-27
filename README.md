# gpt-resolve
Can GPT solve Brazilian university entrance exams?

This project is an implementation of how to use LLMs to solve challenging Brazilian university entrance exams.

We started with `o1-preview`, and `gpt-4o` to describe the exam images so that `o1-preview` could solve them, because it did not have image capabilities yet. Now that reasoning models are processing images as well, we've updated the code to process them directly. Also, we've started solutions with `o1` and hope to add other models as well. Results are saved as txt files with LaTeX formatting, and you can optionally convert them to a nice PDF with this package or using some LaTeX editor.

The project begins with the ITA (Instituto Tecnológico de Aeronáutica) 2025 exam, focusing first on the Math essay section. This section, from the recent exam on November 5, 2024, demands deep subject understanding and step-by-step solutions. More details are in the [report](exams/ita_2025/report.md) documentation.

**Spoilers: o1-preview scored 90% in the ITA 2025 Math Essay Exam, 95% in Chemistry Essay and only 65% in Physics Essay. o1 scored 95% in the same Math exam.**

After the first ITA 2025 exam is fully solved, the project will try to expand to other sections and eventually other exams. Feel free to contribute with ideas and implementations of other exams!

Table of some exams to be solved:

| Exam         | Year | Status        | Score | Report                             |
| ------------ | ---- | ------------- | ----- | ---------------------------------- |
| ITA          | 2025 | 🚧 In Progress | -     | [Report](exams/ita_2025/report.md) |
| IME          | 2025 | 📅 Todo        | -     | -                                  |
| Escola Naval | 2025 | 📅 Todo        | -     | -                                  |
| Fuvest/USP   | 2025 | 📅 Todo        | -     | -                                  |
| AFA          | 2025 | 📅 Todo        | -     | -                                  |
| UNICAMP      | 2025 | 📅 Todo        | -     | -                                  |
| ENEM         | 2025 | 📅 Todo        | -     | -                                  |

# Installation and How to use
gpt-resolve is distributed in pypi:
```bash
pip install gpt-resolve
```

`gpt-resolve` provides a simple CLI with two main commands: `resolve` for solving exam questions and `compile-solutions` for generating PDFs from the solutions, as you can check below. During development, install locally with `pip install -e .`.

### Solve exams with `resolve`

Since v0.5, `gpt-resolve` runs on the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), which drives the local `claude` CLI. That means it uses whatever auth your Claude Code has: your Claude subscription (after `claude login`) or `ANTHROPIC_API_KEY`.

How it works:
1. **Extract** (PDF only): an agent reads the exam PDF and lists the questions (number, pages, transcription). Cached in `questions.json`, so re-runs skip it.
2. **Solve**: each question runs in its own agent (default `claude-opus-5-5`), which can read the original pages/figures and use Python to check its work.
3. **Judge**: an adversarial agent (default `claude-opus-5-5`) solves the question independently and scores the *whole resolution* (correctness, completeness, rigor, clarity) from 0 to 10. Below `--pass-score` (default 9), the solver revises using the critique, up to `--max-rounds` (default 3). The best attempt is kept and flagged as approved or not.
4. **Compile**: a PDF with all solutions plus an appendix with each judge score and review (needs `pdflatex`).

```bash
claude login            # once, if using your subscription
pip install -e .
gpt-resolve resolve -p "IME 2027 Matematica.pdf" -q 1,2 -t "IME 2027 - Matemática"
```

Outputs go to `<pdf name>_solutions/<model>/`: `q<n>_solution.txt` (LaTeX), `q<n>_judge.json` (scores and reviews of every round) and `solutions_compiled.pdf`. The old layout of one image per question (`q1.jpg`, ..., optional `conventions.jpg`) still works by passing the folder to `-p`.

Useful options (see `gpt-resolve resolve --help`): `--model`, `--judge-model`, `--pass-score`, `--max-rounds`, `--effort`, `--concurrency`, `--no-compile`, `--dry-run` (offline mock).

Providers live in `src/gpt_resolve/providers/`: implement `Provider.run` and register it in `get_provider` to use another backend (`--provider`).


### Compile solutions with `compile-solutions`

Once you have the solutions in your exam folder `exam_path`, you can compile them into a single PDF running:
```bash
gpt-resolve compile-solutions -p exam_path --title "Your Exam Title --author 'o1 (OpenAI)'"
```

For that command to work, you'll need a LaTeX distribution in your system. See some guidelines [here](https://www.tug.org/texlive/) (MacTeX for MacOS was used to start this project). This project was developed with [MacTeX](https://www.tug.org/mactex/) distribution.

# Troubleshooting

Sometimes, it was observed that the output from `o1-preview` produced invalid LaTeX code when nesting display math environments (such as `\[...\]` and `\begin{align*} ... \end{align*}` together). The current prompt for `o1-preview` adds an instruction to avoid this, which works most of the time. If that happens, you can try to solve the question again by running `gpt-resolve resolve -p exam_path -q <question_number>`, or making more adjustments to the prompt, or fixing the output LaTeX code manually. Experiments with `o1` did not show any similar errors so far.

# Costs

Reasoning models like `o1` are much more expensive than non-reasoning models like `gpt-4o`, consuming much more tokens to "reason" (see more [here](https://platform.openai.com/docs/guides/reasoning/controlling-costs#controlling-costs)), so be mindful about the number of questions you are solving and how many max tokens you're allowing gpt-resolve to use (see `gpt-resolve resolve --help` to control `max-tokens-question-answer`, which drives the cost). You can roughly estimate an upper bound for costs of solving an exam by
```
(number of questions) * (max_tokens_question_answer / 1_000_000) * (price per 1M tokens)
```
For the current price for o1 of $15/$60 per 1M tokens for input/output tokens, an 10 question exam with 10000 max tokens per question would cost less than $6. For `o3`, for which the price is $10/$40 per 1M tokens for input/output tokens, the cost would be less than $4.

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
