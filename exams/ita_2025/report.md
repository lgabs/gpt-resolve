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

| Exam | Phase | Section | Type | Model | Status | Score | PDF Compiled |
|------|-------|---------|------|-------|--------|-------|--------------|
| ITA  | 2025  | Math    | Essay | o1-preview | ✅ Completed | 90%| [PDF](math/essays/solutions/solutions_compiled.pdf) |
| ITA  | 2025  | Physics | Essay | o1-preview | 🚧 TODO | - | - |
| ITA  | 2025  | Chemistry | Essay | o1-preview | ✅ Completed | 95% | [PDF](chemistry/essays/solutions/solutions_compiled.pdf) |
| ITA  | 2025  | Portuguese | Essay | o1-preview | 🚧 TODO | - | - |
| ITA  | 2025  | Math    | Multiple Choice | o1-preview | 🚧 TODO | - | - |

## Score calculation
For multiple-choice exams, the score is straightforward. For essays, each question is valued at 10.0 points. For questions with more than one part, we considered each part equally weighted. Since it's an essay, in some cases, the LLM provided almost correct reasoning but made some mistakes, so we had to assign partial points when reviewing each question (essay exams are inherently more subjective). 

## Comments

### Math Essay
`o1-preview` almost got all questions correct in the Math essay exam. The only question it got wrong was question 10, which is a question about spacial geometry, which is a known area of weakness for LLMs. After running that question several times, it can get it correct sometimes, but not always. Since it did not got it correct in the first try, it was considered wrong. Check one of these correct answers [here](math/essays/solutions/q10_solution_rerun.txt).

For almost of all questions, `max_tokens_question_description=400` and `max_tokens_question_answer=5000` used in `gpt-resolve` was enough, but for some questions (4,5,7,8) it was necessary to run them again since the answer on the first try were not complete due to the limit of max completion tokens processed. In these cases, `max_tokens_question_answer=10000` was used.

### Chemistry Essay

Again, `o1-preview` got all questions correct in the Chemistry essay exam. The only wrong question was question 3, where it got parts (a) and (b) correct, but (c) and (d) wrong. This is probably because parts (c) and (d) involved reasoning about what was represented in the picture of the question, which is hard for LLMs to do, so gpt-4o did some limited description of the image but it was not enough for o1-preview. This is why, for this question, we considered 5.0 points for the score (2 parts out of 4).

`max_tokens_question_answer=5000` worked for most questions; only question 8 could not and so `10000` was used. Also, for some questions the confusion about how to use decimal separators or thousands separators in portuguese or english induced some errors, even when the development was clearly correct. To fix that, we updated the o1-preview prompt to use `,` for decimal separators and avoid thousands separators.
