# One-shot without the judge: IME 2027 and ITA 2027 Physics

An experiment: how well does the solver do on its own, with `--no-judge` (one solver pass per question, no adversarial review, no second round)? Both Physics essay exams were solved in parallel in a cloud container on October 30, 2026, then graded with `gpt-resolve grade` against the same Poliedro answer keys used for the judged runs ([IME 2027](ime_2027/report.md), [ITA 2027](ita_2027/report.md)). The answer keys are not committed.

```bash
gpt-resolve resolve -p exams/ime_2027/physics/essays/exam.pdf -t "IME 2027 - Física (one-shot, sem judge)" \
  -o exams/ime_2027/physics/essays/solutions/claude_opus_5_5_no_judge --no-judge --concurrency 10
gpt-resolve resolve -p exams/ita_2027/physics/essays/exam.pdf -t "ITA 2027 - Física (one-shot, sem judge)" \
  -o exams/ita_2027/physics/essays/solutions/claude_opus_5_5_no_judge --no-judge --concurrency 10
```

Other parameters were the defaults (`claude-opus-5-5`, `--effort xhigh`).

| Exam | Mode | Time (extraction + 10 questions) | Estimated cost to solve | Score vs Poliedro | Solutions | Grade report |
| ---- | ---- | -------------------------------- | ----------------------- | ----------------- | --------- | ------------ |
| IME 2027 Physics | judge | 6.3 min (`--concurrency 4`) | not logged | **100%** (30/30) | [PDF](ime_2027/physics/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](ime_2027/physics/essays/solutions/claude_opus_5_5/grade_report.pdf) |
| IME 2027 Physics | **no judge** | 3.0 min | US$ 2.59 | **100%** (30/30) | [PDF](ime_2027/physics/essays/solutions/claude_opus_5_5_no_judge/solutions_compiled.pdf) | [PDF](ime_2027/physics/essays/solutions/claude_opus_5_5_no_judge/grade_report.pdf) |
| ITA 2027 Physics | judge | 5.2 min (Q4 needed a 2nd round) | not logged | **100%** (24/24) | [PDF](ita_2027/physics/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) | [PDF](ita_2027/physics/essays/solutions/claude_opus_5_5/grade_report.pdf) |
| ITA 2027 Physics | **no judge** | 3.6 min | US$ 3.32 | **100%** (24/24) | [PDF](ita_2027/physics/essays/solutions/claude_opus_5_5_no_judge/solutions_compiled.pdf) | [PDF](ita_2027/physics/essays/solutions/claude_opus_5_5_no_judge/grade_report.pdf) |

Grading cost US$ 1.65 (IME, 0.8 min) and US$ 2.03 (ITA, 1.0 min). The judged runs predate per-agent cost logging; with the judge, a question approved in the first round costs 3 agent sessions (blind judge, solver, review) instead of 1, so roughly 2 to 3 times more.

## Takeaways

- **Same final answers.** Every final answer of the one-shot runs matches the judged runs and the Poliedro key, item by item, on both exams. That includes the two spots where the judge mattered before: ITA Q4 (rejected at 8.5 in round 1 of the judged run, for presentation and hypotheses, not the result) and IME Q7b (the one-shot gives the ratio with its sign, ≈ −1.6).
- **About half the time.** 3.0 and 3.6 minutes against 6.3 and 5.2. The slowest question sets the pace (ITA Q1, 2.8 min).
- **What the judge still buys.** A score per question, a blind second solution to catch errors, and a revision round when the write-up is incomplete or not rigorous enough. On these two exams none of that changed a final answer. The graders did flag small write-up issues in the one-shot solutions (e.g. a sign typo in the Clausius inequality in IME Q5c, conclusion still right), the kind of thing the judge tends to send back.

Two exams are a small sample: these were exams where the judged runs were already near-perfect.
