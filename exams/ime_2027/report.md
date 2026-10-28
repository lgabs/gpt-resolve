# IME 2027 (2nd phase)

The IME 2027 2nd phase took place on October 26 (Math) and October 27, 2026 (Physics). This is the first exam solved with the Claude Agent SDK pipeline (v0.5).

## Physics essay

| Exam | Phase | Section | Type  | Solver            | Judge             | Status   | Judge scores | PDF Compiled |
| ---- | ----- | ------- | ----- | ----------------- | ----------------- | -------- | ------------ | ------------ |
| IME  | 2nd   | Physics | Essay | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 9.5    | [PDF](physics/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) |

Parameters: `--effort xhigh`, `--pass-score 9`, `--max-rounds 3`, `--concurrency 4`, input given as the exam PDF ([exam.pdf](physics/essays/exam.pdf), identical by SHA-256 to the official `FISÍCA_-_DISCURSIVA.pdf` at [inscricoes.ime.eb.br/cfg](https://inscricoes.ime.eb.br/cfg/)). The whole exam (extraction + 10 questions) took 6.3 minutes.

```bash
gpt-resolve resolve -p exams/ime_2027/physics/essays/exam.pdf -t "IME 2027 - Física" \
  -o exams/ime_2027/physics/essays/solutions/claude_opus_5_5
```

All 10 questions were approved by the judge in the first round. For every question, the judge's blind solution (done before seeing the candidate) reached the same final answers as the solver, and the judge raised no critical or major issue, only minor ones (missing explicit hypotheses, steps worth expanding).

| Question | Judge score | Final answer (summary) |
| -------- | ----------- | ---------------------- |
| 1  | 9.5 | a) 250 m/s; b) 4000 K; c) 864 kJ done by the gases |
| 2  | 9.5 | a) A = 200 kN up, B = 100 kN down; b) member forces (AE = 0); c) AE braces panel ADEB |
| 3  | 9.5 | a) 300 N up; b) ΔT = 100 °C; c) breaks at 37.5% of the day (10⁴ s) |
| 4  | 9.2 | a) 900 V, 50 A; b) fuse blows ≈ 1.5 s; c) doesn't protect the generator |
| 5  | 9.5 | a) 450 K; b) 90 kW; c) proposal B violates the 1st and 2nd laws |
| 6  | 9.5 | a) 68 m/s; b) 5√3 m; c) ≈ 1068 N; d) ≈ 55.1 L |
| 7  | 9.2 | a) 0.45 m; b) 29/18; c) P2 arrives first, √2 m/s |
| 8  | 9.5 | a) screen moves away; b) 0.2√7 m; c) ≈ 0.25 m/s; d) ≈ 1.79 m |
| 9  | 9.0 | a) u = c(√3h − L)/(√3L − h); b) L/√3 < h < L |
| 10 | 9.5 | a) only situation 2; b) SHM with ω = (2/d)√(μ₀qiv/(πm)) |

An independent run on a Mac (same parameters, user's Claude subscription) also approved all 10 questions in the first round (scores 9.0 – 9.5) with the same final answers.

**Validation:** the answers were checked during the exam day against a physics teacher who solved the exam independently.

### Comparison with the Poliedro answer key

Graded with `gpt-resolve grade` against the [Poliedro Resolve](https://poliedroresolve.sistemapoliedro.com.br/vestibulares/ime/2027/ime-2-fase-dia-2-27-10-2026-2-fase-dia-2/dissertativa-1-fisica-2-fase-dia-2-ime-2027) solutions (one grader agent per question, 10 in parallel, 1.1 min). Full report: [PDF](physics/essays/solutions/claude_opus_5_5/grade_report.pdf) ([LaTeX](physics/essays/solutions/claude_opus_5_5/grade_report.tex), [Markdown](physics/essays/solutions/claude_opus_5_5/grade_report.md)), per question in `q<n>_grade.json`.

**Final score: 100% (30 of 30 items match the key).** No wrong result was found on either side; every disagreement was redone by the grader.

| Question | Items | Score | Notes |
| -------- | ----- | ----- | ----- |
| 1  | 3 | 10 | |
| 2  | 3 | 10 | c) same argument (AE braces ADEB), ours more detailed |
| 3  | 3 | 10 | |
| 4  | 3 | 10 | b) 1.5 s read from the fuse curve (checked by hand) |
| 5  | 3 | 10 | c) same conclusion; Poliedro frames it as "does not violate the 2nd law" at the feasible 71.7 kW point, ours as the claim violating the 1st law |
| 6  | 4 | 10 | |
| 7  | 3 | 10 | b) Poliedro gives −1.6 (signed ΔU_g), our final line gives the magnitude 29/18 ≈ 1.6; the statement doesn't say which |
| 8  | 4 | 10 | |
| 9  | 2 | 10 | |
| 10 | 2 | 10 | |

The open points (hypotheses not stated in the statement, graph readings, sign conventions) are listed at the end of the grade report.

## Math essay

| Exam | Phase | Section | Type  | Solver            | Judge             | Status   | Judge scores | PDF Compiled |
| ---- | ----- | ------- | ----- | ----------------- | ----------------- | -------- | ------------ | ------------ |
| IME  | 2nd   | Math    | Essay | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.5 (all)    | [PDF](math/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) |

Same parameters as the physics run (`--effort xhigh`, `--pass-score 9`, `--max-rounds 3`), with `--concurrency 10`. The whole exam (extraction + 10 questions) took 3.5 minutes in a cloud container, and all 10 questions were approved by the judge in the first round (9.5 each, only minor issues).

```bash
gpt-resolve resolve -p exams/ime_2027/math/essays/exam.pdf -t "IME 2027 - Matemática" \
  -o exams/ime_2027/math/essays/solutions/claude_opus_5_5 --concurrency 10
```

The exam PDF ([exam.pdf](math/essays/exam.pdf)) is the official one: same SHA-256 (`a4888009…cfbb3`) as `MATEMÁTICA_-_DISCURSIVA.pdf` published at [inscricoes.ime.eb.br/cfg](https://inscricoes.ime.eb.br/cfg/), section "Informações ao candidato" → "PROVAS - 2ª FASE 2026/2027" (direct link: `https://inscricoes.ime.eb.br/documentos/MATEM%C3%81TICA_-_DISCURSIVA.pdf`; physics is `FIS%C3%8DCA_-_DISCURSIVA.pdf` in the same folder). The IME does not publish an answer key for the essays.

| Question | Judge score | Final answer (summary) |
| -------- | ----------- | ---------------------- |
| 1  | 9.5 | area of P ∪ I = 12√3 − 18 |
| 2  | 9.5 | P = 2/5 |
| 3  | 9.5 | x = 7 |
| 4  | 9.5 | 1345 |
| 5  | 9.5 | with the printed 5540: S ≈ 11196.5 (irrational); flags a likely typo, with 5440: S = 10912 |
| 6  | 9.5 | P = 1/3 |
| 7  | 9.5 | proof: tr(AB) = C(2026, 1001), divisible by 1013 |
| 8  | 9.5 | proof of S_n = sen(nα)/(sen 2α · cos((n+1)α)) |
| 9  | 9.5 | locus 4x²/49 + y² = 1; points (±2√3, ±1/7) |
| 10 | 9.5 | a) 192√3 cm³; b) cube of edge 4√3 cm |

### Comparison with the Poliedro answer key

Graded with `gpt-resolve grade` against the [Poliedro Resolve](https://poliedroresolve.sistemapoliedro.com.br/vestibulares/ime/2027/ime-2-fase-dia-1-26-10-2026-2-fase-dia-1/dissertativa-1-matematica-2-fase-dia-1-ime-2027) solutions (10 grader agents in parallel, 0.8 min). Full report: [PDF](math/essays/solutions/claude_opus_5_5/grade_report.pdf) ([LaTeX](math/essays/solutions/claude_opus_5_5/grade_report.tex), [Markdown](math/essays/solutions/claude_opus_5_5/grade_report.md)).

**Final score: 100% (12 of 12 items match the key).** Notes:

- **Q5:** the official statement prints x2 + x4 + x6 + x8 = 5540, which has no rational answer; Poliedro assumes a typo (5440 → 10912) and suggests annulling the question. Our solution gives both the literal answer (≈ 11196.5) and the 5440 one, so it holds whatever the board decides.
- **Q7:** the final result matches, but the grader found a false step in Poliedro's proof ("1013 does not divide 1025!·1001!"; it does divide 1025!). The correct argument counts the multiplicity of 1013, as our solution does.
- Q3 and Q10: Poliedro skips justifications (x ∈ ℤ+, rectangular base) that our solutions include.
