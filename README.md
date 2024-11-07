# gpt-resolve
Can GPT solve Brazilian university entrance exams?

This project is a simple implementation of how to use GPT to solve challenging Brazilian university entrance exams. 

The first exam to be solved is the ITA (Instituto Tecnológico de Aeronáutica) exam for admissions in 2025, which is considered one of the most challenging exams in Brazil. This exam currently has two phases: the first one is a multiple choice test and a second one with a 4-hour essay test with 10 questions. The project will start by solving the second phase of the Math section, which is the essay test. This is particularly interesting because (i) the exam happened very recently on the 5th of November 2024 and (ii) the essay test requires a deep understanding of the subjects and the ability to write the answer step by step, which we'll evaluate as well.

To simplify the approach for now, we'll use the best OpenAI model with image capabilities: `gpt-4o`. The `o1-preview` model is also a good candidate, since it has reasoning capabilities, but it still lacks the image capabilities for now and the preprocessing of exams would be a bit more complex.

After the first exam is solved, the project will try to solve the multiple choice test for Math and expand to other sections and eventually other exams. Feel free to contribute with ideas and implementations of other exams! 

Table of exams to be solved:

| Exam | Phase | Section | Type | Model | Status |
|------|-------|---------|------|-------|--------|
| ITA  | 2025  | Math    | Essay | GPT-4o | 🚧 In Progress |

