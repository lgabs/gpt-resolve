# Escola Naval 2026 (CPAEN 2026)

The written exams of the Escola Naval admission (CPAEN 2026, for entry in 2027) took place on August 29 and 30, 2026. Day 1 had Math (Q1–22) and English; day 2 had Portuguese and Physics (Q19–40). Only Math and Physics are solved here. All questions are multiple choice (A–E).

The exam PDFs are the official AMARELA booklets, cut to the Math and Physics pages. They are scanned, with no text layer, so the agents read the page images. They were solved with the Claude Agent SDK pipeline, the same way as [ITA 2027](../ita_2027/report.md): the solver and the judge only see the exam PDF, never an answer key. The comparison with the official answer key (preliminary key published by the SSPM on September 1, 2026, AMARELA column) is a separate step (`gpt-resolve grade`) run after the solutions were approved.

| Exam         | Section | Type            | Solver            | Judge             | Status   | Judge scores | Official key       | PDF Compiled |
| ------------ | ------- | --------------- | ----------------- | ----------------- | -------- | ------------ | ------------------ | ------------ |
| Escola Naval | Math    | Multiple choice | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 9.5    | 22/22 (100%)       | [PDF](math/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) |
| Escola Naval | Physics | Multiple choice | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 9.5    | 21/22 (95%), see Q34 | [PDF](physics/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) |

Parameters: `--effort xhigh`, `--pass-score 9`, `--max-rounds 3`, `--concurrency 8`, run in a cloud container. All 44 questions were approved by the judge in the first round. Math took 5.2 minutes and Physics 7.0 minutes (both in parallel). Estimated cost at API prices, as reported by the agents: US$ 9.50 (Math) + US$ 11.07 (Physics) to solve, plus US$ 2.45 + US$ 3.04 to grade.

Highlights from the grading:

- **Physics Q34: our answer (B) differs from the preliminary key (E), and the grader agrees with ours.** From the graph, k = 20 N/m. Since friction only has to accelerate m₂, the maximum deformation without slipping is 30 cm (not 20 cm), and the period is 2π√(3/20) ≈ 2.43 s (not 0.4π√5 ≈ 2.81 s), so all three statements are false. The key's 20 cm comes from the classic mistake k·d = μ·m₁·g. It is worth checking whether the final key changed it.
- **Math Q2**: our answer matches the key (A), but the solution points out that, read literally, the ratio smallest/largest real root is (7 − 3√5)/2 ≈ 0.146, which is not among the options; (A) is the common ratio of the roots' geometric progression. Marked (A) as a forced choice.
- **Math Q12** was annulled by the board: it is a verbatim repeat of Q5 in the booklet.

## Math

```bash
gpt-resolve resolve -p exams/escola_naval_2026/math/multiple_choice/exam.pdf -t "Escola Naval 2026 (CPAEN) - Matemática" \
  -o exams/escola_naval_2026/math/multiple_choice/solutions/claude_opus_5_5 --concurrency 8
gpt-resolve grade -p exams/escola_naval_2026/math/multiple_choice/solutions/claude_opus_5_5 \
  -k key_en2026_matematica.json -e exams/escola_naval_2026/math/multiple_choice/exam.pdf
```

Full grade report: [PDF](math/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) ([Markdown](math/multiple_choice/solutions/claude_opus_5_5/grade_report.md)).

| Question | Judge score | Our answer | Official key | Match |
| -------- | ----------- | ---------- | ------------ | ----- |
| 1 | 9.5 | D | D | ✅ |
| 2 | 9.5 | A | A | ✅ |
| 3 | 9.5 | C | C | ✅ |
| 4 | 9.5 | B | B | ✅ |
| 5 | 9.5 | E | E | ✅ |
| 6 | 9.5 | B | B | ✅ |
| 7 | 9.5 | A | A | ✅ |
| 8 | 9.5 | A | A | ✅ |
| 9 | 9.5 | A | A | ✅ |
| 10 | 9.3 | E | E | ✅ |
| 11 | 9 | B | B | ✅ |
| 12 | 9 | E | Annulled | ✅ |
| 13 | 9 | C | C | ✅ |
| 14 | 9.5 | B | B | ✅ |
| 15 | 9 | B | B | ✅ |
| 16 | 9.5 | D | D | ✅ |
| 17 | 9.5 | A | A | ✅ |
| 18 | 9.5 | A | A | ✅ |
| 19 | 9.5 | A | A | ✅ |
| 20 | 9 | D | D | ✅ |
| 21 | 9.5 | E | E | ✅ |
| 22 | 9.5 | D | D | ✅ |

## Physics

```bash
gpt-resolve resolve -p exams/escola_naval_2026/physics/multiple_choice/exam.pdf -t "Escola Naval 2026 (CPAEN) - Física" \
  -o exams/escola_naval_2026/physics/multiple_choice/solutions/claude_opus_5_5 --concurrency 8
gpt-resolve grade -p exams/escola_naval_2026/physics/multiple_choice/solutions/claude_opus_5_5 \
  -k key_en2026_fisica.json -e exams/escola_naval_2026/physics/multiple_choice/exam.pdf
```

Full grade report: [PDF](physics/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) ([Markdown](physics/multiple_choice/solutions/claude_opus_5_5/grade_report.md)).

| Question | Judge score | Our answer | Official key | Match |
| -------- | ----------- | ---------- | ------------ | ----- |
| 19 | 9 | D | D | ✅ |
| 20 | 9.5 | E | E | ✅ |
| 21 | 9.5 | A | A | ✅ |
| 22 | 9.5 | A | A | ✅ |
| 23 | 9.5 | B | B | ✅ |
| 24 | 9.5 | E | E | ✅ |
| 25 | 9.5 | D | D | ✅ |
| 26 | 9.5 | C | C | ✅ |
| 27 | 9.5 | A | A | ✅ |
| 28 | 9 | B | B | ✅ |
| 29 | 9.5 | A | A | ✅ |
| 30 | 9.3 | D | D | ✅ |
| 31 | 9.5 | C | C | ✅ |
| 32 | 9.5 | E | E | ✅ |
| 33 | 9.5 | C | C | ✅ |
| 34 | 9.5 | B | E | ⚠️ key looks wrong |
| 35 | 9.5 | D | D | ✅ |
| 36 | 9.5 | B | B | ✅ |
| 37 | 9.5 | B | B | ✅ |
| 38 | 9.5 | C | C | ✅ |
| 39 | 9.5 | E | E | ✅ |
| 40 | 9.5 | D | D | ✅ |
