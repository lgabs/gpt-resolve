# ITA 2027 (2nd phase)

The ITA 2027 2nd phase essays took place on October 20 (Math), October 21 (Chemistry) and October 22, 2026 (Physics), with Portuguese on October 23 (not solved here). Each essay exam has 10 questions. They were solved with the Claude Agent SDK pipeline (v0.6), the same way as [IME 2027](../ime_2027/report.md): the solver and the judge only see the exam PDF, never an answer key, and the comparison with the Poliedro solutions is a separate step (`gpt-resolve grade`) run after the solutions were approved.

The exam PDFs are the official ones, `https://www.vestibular.ita.br/provas/<subject>_2027_2f.pdf` (`matematica`, `quimica`, `fisica`). As of October 29, 2026 they are not yet linked on [vestibular.ita.br/provas.htm](https://www.vestibular.ita.br/provas.htm), and the official answer key (`gabarito_2027_2f.pdf`) is not published yet. Poliedro publishes byte-identical copies of the three PDFs.

| Exam | Phase | Section   | Type  | Solver            | Judge             | Status   | Judge scores | Score vs Poliedro | PDF Compiled |
| ---- | ----- | --------- | ----- | ----------------- | ----------------- | -------- | ------------ | ----------------- | ------------ |
| ITA  | 2nd   | Math      | Essay | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.5 – 10     | 100% (12/12 items) | [PDF](math/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) |
| ITA  | 2nd   | Chemistry | Essay | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 9.5    | 99% (36/37 items)  | [PDF](chemistry/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) |
| ITA  | 2nd   | Physics   | Essay | `claude-opus-5-5` | `claude-opus-5-5` | ✅ Solved | 9.0 – 9.5    | 100% (24/24 items) | [PDF](physics/essays/solutions/claude_opus_5_5/solutions_compiled.pdf) |

Parameters for all three: `--effort xhigh`, `--pass-score 9`, `--max-rounds 3`, `--concurrency 10`, run in a cloud container. 29 of the 30 questions were approved by the judge in the first round; only Physics Q4 needed a second round (8.5 → 9.5).

The score vs Poliedro is the share of items where the grader found our answer right (matching or equivalent to the key, or the key wrong); within a question every item weighs the same. The answer keys follow the format described in the [README](../../README.md#compare-with-an-answer-key-grade) (final answer per item + the worked resolution, based on the public [Poliedro Resolve](https://poliedroresolve.sistemapoliedro.com.br/vestibulares/ita/2027) solutions) and are not committed. Several "typos in the key" listed in the grade reports come from writing the formulas as plain text in the key file, not from Poliedro itself.

## Math essay

```bash
gpt-resolve resolve -p exams/ita_2027/math/essays/exam.pdf -t "ITA 2027 - Matemática" \
  -o exams/ita_2027/math/essays/solutions/claude_opus_5_5 --concurrency 10
```

The whole exam (extraction + 10 questions) took 2.6 minutes. All 10 questions were approved in the first round, with only minor issues.

| Question | Judge score | Final answer (summary) |
| -------- | ----------- | ---------------------- |
| 1  | 9.5 | 10 APs: r = ±1, ±3, ±5, ±7, ±9 (5 increasing and the same 5 decreasing) |
| 2  | 9.5 | log₂((√5 − 1)/2) < x < 1 |
| 3  | 9.5 | r = 1/16, side √(4 − 2√2)/2 |
| 4  | 9.5 | a = −2; roots −1 (double), 2, ±i, 3 ± 2√2 |
| 5  | 9.5 | x_C = 5√3 − 9 |
| 6  | 9.5 | 235 |
| 7  | 10  | n ∈ {−6, −4, 6, 8} |
| 8  | 9.5 | a) 0 < x ≤ 1 or 9 ≤ x < 10; b) sides √10 and 3√10 |
| 9  | 9.5 | area 10 + 5√3 |
| 10 | 9.5 | k = 3 |

### Comparison with the Poliedro answer key

Graded against [Poliedro Resolve](https://poliedroresolve.sistemapoliedro.com.br/vestibulares/ita/2027/ita-2-fase-dia-1-20-10-2026-2-fase-dia-1/dissertativa-1-matematica-2-fase-dia-1-ita-2027) (10 grader agents in parallel, 1.1 min). Full report: [PDF](math/essays/solutions/claude_opus_5_5/grade_report.pdf) ([LaTeX](math/essays/solutions/claude_opus_5_5/grade_report.tex), [Markdown](math/essays/solutions/claude_opus_5_5/grade_report.md)).

**Final score: 100% (12 of 12 items match the key).** Every final answer matches. In Q1 our solution also justifies why the common difference stops at ±9 (a₁ ≥ 1 and a₁₀ ≥ 1, with ℕ = {1, 2, 3, …} as the exam defines), which the key only lists.

## Chemistry essay

```bash
gpt-resolve resolve -p exams/ita_2027/chemistry/essays/exam.pdf -t "ITA 2027 - Química" \
  -o exams/ita_2027/chemistry/essays/solutions/claude_opus_5_5 --concurrency 10
```

The whole exam took 4.7 minutes. All 10 questions were approved in the first round.

| Question | Judge score | Final answer (summary) |
| -------- | ----------- | ---------------------- |
| 1  | 9.5 | a) C₅H₁₂ + 8 O₂ → 5 CO₂ + 6 H₂O; b) 1.6 mol O₂, 6.4 mol N₂; c) 2300.84 K; d) 37% less fuel |
| 2  | 9.5 | π = 5.008/(10 − x) atm up to x = 6 dm (saturation), then constant ≈ 1.25 atm |
| 3  | 9.5 | X 2-methylbut-2-ene; Z 2-bromo-2-methylbutane; G 2-bromo-3-methylbutane; J 2-methylbutane-2,3-diol |
| 4  | 9.5 | a) 40 g; b) 75%; c) 180 g/mol; d) 3.0 mol/L |
| 5  | 9.5 | N₂ + 8 H⁺ + 6 e⁻ → 2 NH₄⁺; oxidation numbers; N₂ → NH₄⁺ → NO₂⁻ → NO₃⁻ → NO₂⁻ → NO → N₂O → N₂ |
| 6  | 9.0 | Li + H₂O, steam reforming, methane pyrolysis; most H₂ per mol: pyrolysis |
| 7  | 9.5 | ΔH° = −496.2 kJ/mol, ΔS° = −127.2 J/(K·mol), ΔG° ≈ −458.3 kJ/mol |
| 8  | 9.5 | 2, 2 unpaired e⁻ (S, Se), 1 valence e⁻ (K); 2 and 1 lone pairs; bent and seesaw |
| 9  | 9.5 | [HX] = 8.0·10⁻³ mol/L, [HY] = 1.2·10⁻² mol/L |
| 10 | 9.0 | cathode/anode regions in the 4 cells; protection: cathodic in 1, 3, 4, anodic in 2 |

### Comparison with the Poliedro answer key

Graded against [Poliedro Resolve](https://poliedroresolve.sistemapoliedro.com.br/vestibulares/ita/2027/ita-2-fase-dia-2-21-10-2026-2-fase-dia-2/dissertativa-1-quimica-2-fase-dia-2-ita-2027) (1.3 min). Full report: [PDF](chemistry/essays/solutions/claude_opus_5_5/grade_report.pdf) ([LaTeX](chemistry/essays/solutions/claude_opus_5_5/grade_report.tex), [Markdown](chemistry/essays/solutions/claude_opus_5_5/grade_report.md)).

**Final score: 99% (36 of 37 items; average 9.9/10 per question).**

- **Q10 b(2), wrong:** for the bar between an alkaline (X) and an acidic (Y) region, our solution recommends anodic protection; Poliedro says cathodic, as in the other three cells. The grader sides with Poliedro: at low pH iron has no passive domain (Pourbaix), so anodic polarization would speed up corrosion at Y, which our own item a(2) argues.
- **Q6, counted right but different:** the question is open (any three reactions). Our third reaction is methane pyrolysis (CH₄ → C + 2 H₂) instead of Poliedro's water electrolysis, so our "most H₂ per mol" answer is pyrolysis (2 mol H₂/mol) instead of steam reforming (1.5 mol). Both are consistent with their own choices.
- Q3: Poliedro notes that the statement uses H₂O₂ for the peroxide effect (HBr anti-Markovnikov addition); both answers read it that way.

## Physics essay

```bash
gpt-resolve resolve -p exams/ita_2027/physics/essays/exam.pdf -t "ITA 2027 - Física" \
  -o exams/ita_2027/physics/essays/solutions/claude_opus_5_5 --concurrency 10
```

The whole exam took 5.2 minutes. Q4 was rejected in the first round (8.5) and approved in the second (9.5); the other 9 were approved in the first round.

| Question | Judge score | Final answer (summary) |
| -------- | ----------- | ---------------------- |
| 1  | 9.5 | a) k_c = MgL/2; b) 1 stable / 3 (1 unstable + 2 stable) / 1 unstable equilibria for k/k_c ≥ 1, 2/π < k/k_c < 1, ≤ 2/π; c) U(θ) sketches |
| 2  | 9.5 | a) H_n = 0.49ⁿ V²/(8g); b) Δt = 10V/(3g) |
| 3  | 9.5 | a) D = √(R² + (2hR/g)√(μₑ²g² − α²R²)); b) stopping time t_slip + √(2h/g) + t_brake |
| 4  | 9.5 | a) h_f = h_i(1 + M/m)^(3/5); b) m(h_max − h_i) = (3/2)(m + M)h_i[1 − (h_i/h_max)^(2/3)] |
| 5  | 9.5 | a) p' = −n₂pR/(n₁R + (n₂ − n₁)p), y' = ±n₁Rh/(n₁R + (n₂ − n₁)p); b) λD/(2n₂h) |
| 6  | 9.5 | a) 3Cε/4; b) compressed by 2d/3; c) k = 27Cε²/(64d²) |
| 7  | 9.0 | a) (V_s/4)\|Gε + αΔT\|; b) 4 strain gauges, R₂ and R₃ in tension, R₁ and R₄ in compression |
| 8  | 9.5 | a) √(2qV/m); b) uniform helix; c) cos θ = (BL/(2πn))√(q/(2mV)) |
| 9  | 9.5 | a) E₀[1 + (−1)ⁿ] cos(kx − ωt) ẑ; b) n even constructive, n odd destructive; c) B = −B₀ cos(kx − ωt) ŷ |
| 10 | 9.5 | a) Compton ν'; b) observer moving against the scattered photon, β = (ν² − ν'²)/(ν² + ν'²) |

### Comparison with the Poliedro answer key

Graded against [Poliedro Resolve](https://poliedroresolve.sistemapoliedro.com.br/vestibulares/ita/2027/ita-2-fase-dia-3-22-10-2026-2-fase-dia-3/dissertativa-1-fisica-2-fase-dia-3-ita-2027) (1.5 min). Full report: [PDF](physics/essays/solutions/claude_opus_5_5/grade_report.pdf) ([LaTeX](physics/essays/solutions/claude_opus_5_5/grade_report.tex), [Markdown](physics/essays/solutions/claude_opus_5_5/grade_report.md)).

**Final score: 100% (24 of 24 items match the key).** Notes:

- **Q4 b):** Poliedro says the statement does not give enough data, since the gas is not in equilibrium at the highest point after the sand is removed at once, and offers two readings. Our answer assumes a reversible adiabatic expansion and is algebraically the same as Poliedro's first reading (the grader checked the roots numerically).
- Q3 and Q10 b): same results written in different algebraic forms.
- Q8 c): our solution states the n > … bound strictly, Poliedro uses ≥; it only matters in the degenerate case θ = 0.
