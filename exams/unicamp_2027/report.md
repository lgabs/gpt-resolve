# Unicamp 2027 (1st phase)

The Unicamp 2027 1st phase (Conhecimentos Gerais) took place on October 18, 2026: 72 multiple-choice questions (A–D) covering every subject, from Portuguese, literature, history, geography, philosophy and sociology to math, physics, chemistry and biology. The whole exam is solved here, including the humanities questions. The 2nd phase is on November 29 and 30.

The exam PDF is the official booklet for versions Q and Y, from [Comvest](https://www.comvest.unicamp.br). It was solved with the Claude Agent SDK pipeline, the same way as [ITA 2027](../ita_2027/report.md): the solver and the judge only see the exam PDF, never an answer key. The comparison with the official answer key (Comvest, versions Q/Y; no question was annulled) is a separate step (`gpt-resolve grade`).

| Exam    | Phase | Type            | Solver            | Judge             | Status   | Judge scores | Official key  | PDF Compiled |
| ------- | ----- | --------------- | ----------------- | ----------------- | -------- | ------------ | ------------- | ------------ |
| Unicamp | 1st   | Multiple choice | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 10     | 72/72 (100%)  | [PDF](first_phase/solutions/claude_opus_5_5/solutions_compiled.pdf) |

```bash
gpt-resolve resolve -p exams/unicamp_2027/first_phase/exam.pdf -t "Unicamp 2027 - 1ª fase (Conhecimentos Gerais, prova Q/Y)" \
  -o exams/unicamp_2027/first_phase/solutions/claude_opus_5_5 --concurrency 12
gpt-resolve grade -p exams/unicamp_2027/first_phase/solutions/claude_opus_5_5 \
  -k key_unicamp2027_f1.json -e exams/unicamp_2027/first_phase/exam.pdf
```

Parameters: `--effort xhigh`, `--pass-score 9`, `--max-rounds 3`, `--concurrency 12`, run in a cloud container. The extraction of the 72 questions took 7 minutes and the whole run 18.7 minutes. 69 of the 72 questions were approved in the first round; Q1 and Q54 needed a second round and Q53 a third. Estimated cost at API prices, as reported by the agents: US$ 33.49 to solve and US$ 7.22 to grade (1.6 minutes).

**Final score: 100% (72 of 72 answers match the official key).**

Full grade report: [PDF](first_phase/solutions/claude_opus_5_5/grade_report.pdf) ([Markdown](first_phase/solutions/claude_opus_5_5/grade_report.md)).

| Question | Judge score | Our answer | Official key | Match |
| -------- | ----------- | ---------- | ------------ | ----- |
| 1 | 9 | B | B | ✅ |
| 2 | 9.5 | C | C | ✅ |
| 3 | 9.5 | C | C | ✅ |
| 4 | 9 | C | C | ✅ |
| 5 | 9 | B | B | ✅ |
| 6 | 9 | B | B | ✅ |
| 7 | 9.5 | A | A | ✅ |
| 8 | 9.2 | A | A | ✅ |
| 9 | 9.5 | B | B | ✅ |
| 10 | 9.5 | D | D | ✅ |
| 11 | 9.5 | A | C | ✅ |
| 12 | 9.5 | C | C | ✅ |
| 13 | 9.5 | D | D | ✅ |
| 14 | 9.5 | B | B | ✅ |
| 15 | 10 | A | A | ✅ |
| 16 | 9.5 | D | D | ✅ |
| 17 | 9.5 | B | B | ✅ |
| 18 | 9.5 | C | C | ✅ |
| 19 | 9.5 | D | D | ✅ |
| 20 | 9.5 | C | C | ✅ |
| 21 | 10 | A | A | ✅ |
| 22 | 9.5 | B | B | ✅ |
| 23 | 9.5 | C | C | ✅ |
| 24 | 9.5 | D | D | ✅ |
| 25 | 9.5 | D | D | ✅ |
| 26 | 9 | A | A | ✅ |
| 27 | 9.5 | D | D | ✅ |
| 28 | 9.5 | B | B | ✅ |
| 29 | 9 | D | D | ✅ |
| 30 | 9.5 | A | A | ✅ |
| 31 | 9.5 | C | C | ✅ |
| 32 | 9.5 | B | B | ✅ |
| 33 | 9 | C | C | ✅ |
| 34 | 9.5 | D | D | ✅ |
| 35 | 9.5 | C | C | ✅ |
| 36 | 9 | D | D | ✅ |
| 37 | 9 | B | B | ✅ |
| 38 | 9.1 | C | C | ✅ |
| 39 | 9 | B | B | ✅ |
| 40 | 9 | D | D | ✅ |
| 41 | 9 | C | C | ✅ |
| 42 | 9.5 | A | A | ✅ |
| 43 | 9 | C | C | ✅ |
| 44 | 9.5 | B | B | ✅ |
| 45 | 9 | C | C | ✅ |
| 46 | 9 | B | B | ✅ |
| 47 | 9.5 | D | D | ✅ |
| 48 | 9.5 | C | C | ✅ |
| 49 | 9.5 | D | D | ✅ |
| 50 | 9 | B | B | ✅ |
| 51 | 9 | A | A | ✅ |
| 52 | 9 | A | A | ✅ |
| 53 | 9.5 | A | A | ✅ |
| 54 | 9 | C | C | ✅ |
| 55 | 9 | A | A | ✅ |
| 56 | 9 | B | B | ✅ |
| 57 | 9 | A | A | ✅ |
| 58 | 9 | C | C | ✅ |
| 59 | 9 | B | B | ✅ |
| 60 | 9.5 | C | C | ✅ |
| 61 | 9.3 | D | D | ✅ |
| 62 | 9.3 | D | D | ✅ |
| 63 | 9.5 | A | A | ✅ |
| 64 | 9.5 | B | B | ✅ |
| 65 | 9.5 | D | D | ✅ |
| 66 | 9.5 | C | C | ✅ |
| 67 | 9.5 | B | B | ✅ |
| 68 | 9.5 | B | B | ✅ |
| 69 | 9.5 | D | D | ✅ |
| 70 | 9.5 | D | D | ✅ |
| 71 | 9.3 | C | C | ✅ |
| 72 | 9.5 | A | A | ✅ |
