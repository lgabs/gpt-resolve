# ITA 2025 Exam Report

## Overview
The Instituto Tecnológico de Aeronáutica (ITA) entrance exam for 2025 consists of two phases:

- **Phase 1**:
  - The exam includes 48 multiple-choice questions, divided into:
    - 12 questions in Mathematics
    - 12 questions in Physics
    - 12 questions in Chemistry
    - 12 questions in English

- **Phase 2**:
  - Essay exams in Mathematics, Physics, and Chemistry, each consisting of 10 questions.
  - An argumentative essay.
  - 15 objective questions in Portuguese.

See more details in the [official exam announcemnt](https://vestibular.ita.br/instrucoes/edital_2025.pdf).

## Results

Preliminary solutions can be found by widely known high schools like [Poliedro](https://poliedroresolve.sistemapoliedro.com.br/vestibulares/ita?year=2025) or [Elite](https://www.colegioecursoelite.com.br/confira-o-gabarito-extraoficial-da-2a-fase-do-ita-2024-2025/). Official solutions will be released soon.

| Exam | Phase | Section    | Type            | Model      | Status      | Score | PDF Compiled                                             |
| ---- | ----- | ---------- | --------------- | ---------- | ----------- | ----- | -------------------------------------------------------- |
| ITA  | 2025  | Math       | Essay           | o1-preview | ✅ Completed | 90%   | [PDF](math/essays/solutions/solutions_compiled.pdf)      |
| ITA  | 2025  | Physics    | Essay           | o1-preview | ✅ Completed | 65%   | [PDF](physics/essays/solutions/solutions_compiled.pdf)   |
| ITA  | 2025  | Chemistry  | Essay           | o1-preview | ✅ Completed | 95%   | [PDF](chemistry/essays/solutions/solutions_compiled.pdf) |
| ITA  | 2025  | Portuguese | Essay           | o1-preview | 🚧 TODO      | -     | -                                                        |
| ITA  | 2025  | Math       | Multiple Choice | o1-preview | 🚧 TODO      | -     | -                                                        |
| ITA  | 2025  | Math       | Essay           | o1         | ✅ Completed | 95%   | [PDF](math/essays/solutions/o1/solutions_compiled.pdf)   |
| ITA  | 2025  | Math       | Essay           | o3         | ✅ Completed | 98%  | [PDF](math/essays/solutions/o3/solutions_compiled.pdf)   |
| ITA  | 2025  | Math       | Essay           | o4-mini    | ✅ Completed | 98%  | [PDF](math/essays/solutions/o4_mini/solutions_compiled.pdf)   |

## Score calculation
For multiple-choice exams, the score is straightforward. For essays, each question is valued at 10.0 points. For questions with more than one part, we considered each part equally weighted. Since it's an essay, in some cases, the LLM provided almost correct reasoning but made some mistakes, so we had to assign partial points when reviewing each question (essay exams are inherently more subjective).

## Comments

### Math Essay
`o1-preview` almost got all questions correct in the Math essay exam. The only question it got wrong was question 10, which is a question about spacial geometry, which is a known area of weakness for LLMs. After running that question several times, it can get it correct sometimes, but not always. Since it did not got it correct in the first try, it was considered wrong. Check one of these correct answers [here](math/essays/solutions/q10_solution_rerun.txt).

For almost of all questions, `max_tokens_question_description=400` and `max_tokens_question_answer=5000` used in `gpt-resolve` was enough, but for some questions (4,5,7,8) it was necessary to run them again since the answer on the first try were not complete due to the limit of max completion tokens processed. In these cases, `max_tokens_question_answer=10000` was used.

The `o1` model, in the other hand, got question 10 correctly with analytic geometry, but in question 7 it failed partially, achieving 95% at the exam. An interesting thing is that this model is much more objetive than the previous version.

New models `o3` and `o4-mini` scored almost 100%, but they failed a bit in question 7 again, but with less errors than `o1`.

### Chemistry Essay

Again, `o1-preview` got all questions correct in the Chemistry essay exam. The only wrong question was question 3, where it got parts (a) and (b) correct, but (c) and (d) wrong. This is probably because parts (c) and (d) involved reasoning about what was represented in the picture of the question, which is hard for LLMs to do, so gpt-4o did some limited description of the image but it was not enough for o1-preview. This is why, for this question, we considered 5.0 points for the score (2 parts out of 4).

`max_tokens_question_answer=5000` worked for most questions; only question 8 could not and so `10000` was used. Also, for some questions the confusion about how to use decimal separators or thousands separators in portuguese or english induced some errors, even when the development was clearly correct. To fix that, we updated the o1-preview prompt to use `,` for decimal separators and avoid thousands separators.

### Physics Essay

This exam was the hardest one so far. o1-preview got only 65% of the questions correct. Here are some details for wrong answers:

- Question 3: failed all three parts. It made a incorrect assumption about the relation between accelerations when the llm said `a_{\text{mov}} = a_{\text{fixa}} - a_M \, \sin\alpha`. 0 points.
- Question 4: failed on part b, when it treated the difference in kinetic energy `\delta` as a positive value (it said `\delta = \frac{E_{\text{inicial}} - E_{\text{final}}}{E_{\text{inicial}}}`, instead of negative value, which would be correct if the llm said `\delta = \frac{E_{\text{final}} - E_{\text{inicial}}}{E_{\text{inicial}}}`. Considering each part valued at `10/3=3.33 points`, we could consider only half for part (b) for the mistake. `total points: 3.33 * 2 + 3.33/2=8.33`
- Question 5: failed on part (b). When the llm said the `v_{\text{NS}} &= v_0 + v_e`, this is only valid if `m<<M`. Checking the solution, we can see that `v_{\text{NS}} &= v_0 + \frac{M}{M+m} \cdot v_e`, i.e., o1 would be correct only if `m<<M` (which is probably true in real life, but the problem statement does not says that. `total points: 5`
- Question 7: pass partially. For part (b), it got the equations to plot intensity right, but o1 is not so good yet to follow instructions to make LaTeX code to really plot images when solving the question.  We can discount points since it did not make graphs, but when asking o1 directly only to plot the images from equations obtained, it produced correct graphs, which we'll include to present a better solution. Discounting half points in (b): `total points: 3.33 + 3.33/2 + 3.33=8.33`.
- Question 8: failed in parts (b) and (c). o1-preview understood how the forces would act in the system, but it did not understand that `\omega` was not given in the problem statement and used it to answer (b). Part (c) was a terrible answer, it expressed `\omega` in terms of `F_{\text{resultante}` and then showed this force in terms of `\omega`, which is  a circular reference. `total points: 3.33 + 0 + 0 = 3.33`.
- Question 9: failed. This question involves a complex image, which we know can affect performance. First, when establishing the equilibrium of the balance, it did not consider the counterweight. Second, GPT-4 was unable to describe the image in a way that allowed the angular coefficient to be calculated, so o1 organized its solution in terms of an unknown coefficient S. `total points: 0`.

Total points so far: `(10+10+0+8.33+5+10+8.33+3.33+0+10) / 10 = 6.50`
