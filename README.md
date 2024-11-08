# gpt-resolve
Can GPT solve Brazilian university entrance exams?

This project is a simple implementation of how to use LLMs to solve challenging Brazilian university entrance exams. 

Particularly, we'll use `o1-preview`, which is the best OpenAI model so far with reasoning capabilities, and `gpt-4o` to describe the exam images so that `o1-preview` can solve them (as it does not have image capabilities yet).

The first exam to be solved is the ITA (Instituto Tecnológico de Aeronáutica) exam for admissions in 2025, which is considered one of the most challenging exams in Brazil. This exam currently has two phases: the first one is a multiple choice test and a second one with a 4-hour essay test with 10 questions. The project will start by solving the second phase of the Math section, which is the essay test. This is particularly interesting because (i) the exam happened very recently on the 5th of November 2024 and (ii) the essay test requires a deep understanding of the subjects and the ability to write the answer step by step, which we'll evaluate as well.

After the first exam is solved, the project will try to solve the multiple choice test for Math and expand to other sections and eventually other exams. Feel free to contribute with ideas and implementations of other exams! 

Table of exams to be solved:

| Exam | Phase | Section | Type | Model | Status |
|------|-------|---------|------|-------|--------|
| ITA  | 2025  | Math    | Essay | o1-preview | 🚧 In Progress |

## Contributing

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

