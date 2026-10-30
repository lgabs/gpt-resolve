# AFA 2027 (EA CFOAV/CFOINT/CFOINF 2027)

The AFA admission exam (Exame de Admissão aos CFOAV/CFOINT/CFOINF 2027) took place on July 5, 2026, in a single booklet with 64 multiple-choice questions (A–D): Portuguese (Q1–16), Math (Q17–32), English (Q33–48) and Physics (Q49–64). Only Math and Physics are solved here; the question numbers are the ones printed in the booklet.

The exam PDF is the official Versão A booklet, cut to the Math and Physics pages. It was solved with the Claude Agent SDK pipeline, the same way as [ITA 2027](../ita_2027/report.md): the solver and the judge only see the exam PDF, never an answer key. The comparison with the official answer key (gabarito oficial, Versão A) is a separate step (`gpt-resolve grade`).

| Exam | Section | Type            | Solver            | Judge             | Status   | Judge scores | Official key       | PDF Compiled |
| ---- | ------- | --------------- | ----------------- | ----------------- | -------- | ------------ | ------------------ | ------------ |
| AFA  | Math    | Multiple choice | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 9.5    | 15/16 (94%), see Q22 | [PDF](math/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) |
| AFA  | Physics | Multiple choice | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 9.5    | 16/16 (100%)       | [PDF](physics/multiple_choice/solutions/claude_opus_5_5/solutions_compiled.pdf) |

Parameters: `--effort xhigh`, `--pass-score 9`, `--max-rounds 3`, `--concurrency 8`, run in a cloud container. 30 of the 32 questions were approved in the first round; Math Q18 needed a second round (8.5 → 9.5) and Q24 a third (8.5 → 8.5 → 9.0). Math took 10.5 minutes and Physics 3.8 minutes (in parallel). Estimated cost at API prices, as reported by the agents: US$ 11.45 (Math) + US$ 6.25 (Physics) to solve, plus US$ 1.85 + US$ 1.30 to grade.

Highlights from the grading:

- **Math Q22: our answer (B) differs from the official key (D), and the grader marks it as unclear.** The computations agree (roots 2, −1, ±5i). It all hinges on statement (II), "há um polígono" whose area divides 5: read literally, the triangle with vertices −1, 5i and −5i has area 5, so (II) is true and the answer is B. The key only holds if the polygon is the quadrilateral with all four roots as vertices (area 15, a multiple of 5, not a divisor), which is what the board most likely meant.
- **Math Q30** was annulled by the board; the grader notes that none of the graphs represents g = −c·f exactly.
- **Math Q26**: the grader flags a contradiction in the statement ("]−L, L[" as the range of a curve whose image is ]0, L[), which did not change the answer.

## Math

```bash
gpt-resolve resolve -p exams/afa_2027/math/multiple_choice/exam.pdf -t "AFA 2027 - Matemática" \
  -o exams/afa_2027/math/multiple_choice/solutions/claude_opus_5_5 --concurrency 8
gpt-resolve grade -p exams/afa_2027/math/multiple_choice/solutions/claude_opus_5_5 \
  -k key_afa2027_matematica.json -e exams/afa_2027/math/multiple_choice/exam.pdf
```

Full grade report: [PDF](math/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) ([Markdown](math/multiple_choice/solutions/claude_opus_5_5/grade_report.md)).

| Question | Judge score | Our answer | Official key | Match |
| -------- | ----------- | ---------- | ------------ | ----- |
| 17 | 9.3 | B | B | ✅ |
| 18 | 9.5 | D | D | ✅ |
| 19 | 9.5 | A | A | ✅ |
| 20 | 9.5 | D | D | ✅ |
| 21 | 9.5 | B | B | ✅ |
| 22 | 9.5 | B | D | ⚠️ ambiguous statement |
| 23 | 9.5 | B | B | ✅ |
| 24 | 9 | A | A | ✅ |
| 25 | 9.5 | A | A | ✅ |
| 26 | 9 | D | D | ✅ |
| 27 | 9.5 | B | B | ✅ |
| 28 | 9.5 | A | A | ✅ |
| 29 | 9.5 | C | C | ✅ |
| 30 | 9.5 | C | Annulled | ✅ |
| 31 | 9.5 | C | C | ✅ |
| 32 | 9.5 | C | C | ✅ |

## Physics

```bash
gpt-resolve resolve -p exams/afa_2027/physics/multiple_choice/exam.pdf -t "AFA 2027 - Física" \
  -o exams/afa_2027/physics/multiple_choice/solutions/claude_opus_5_5 --concurrency 8
gpt-resolve grade -p exams/afa_2027/physics/multiple_choice/solutions/claude_opus_5_5 \
  -k key_afa2027_fisica.json -e exams/afa_2027/physics/multiple_choice/exam.pdf
```

Full grade report: [PDF](physics/multiple_choice/solutions/claude_opus_5_5/grade_report.pdf) ([Markdown](physics/multiple_choice/solutions/claude_opus_5_5/grade_report.md)).

| Question | Judge score | Our answer | Official key | Match |
| -------- | ----------- | ---------- | ------------ | ----- |
| 49 | 9.5 | A | A | ✅ |
| 50 | 9.5 | C | C | ✅ |
| 51 | 9.5 | C | C | ✅ |
| 52 | 9.5 | D | D | ✅ |
| 53 | 9 | D | D | ✅ |
| 54 | 9.1 | D | D | ✅ |
| 55 | 9.5 | B | B | ✅ |
| 56 | 9.5 | B | B | ✅ |
| 57 | 9.5 | B | B | ✅ |
| 58 | 9.3 | C | C | ✅ |
| 59 | 9.5 | C | C | ✅ |
| 60 | 9 | A | A | ✅ |
| 61 | 9.5 | A | A | ✅ |
| 62 | 9.5 | D | D | ✅ |
| 63 | 9.5 | B | B | ✅ |
| 64 | 9.5 | B | B | ✅ |
