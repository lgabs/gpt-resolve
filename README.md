# gpt-resolve
Can GPT solve Brazilian university entrance exams?

This project is a simple implementation of how to use LLMs to solve challenging Brazilian university entrance exams.

We'll use `o1-preview`, which is the best OpenAI model so far with reasoning capabilities, and `gpt-4o` to describe the exam images so that `o1-preview` can solve them (as it does not have image capabilities yet). Results are saved as txt files with LaTeX formatting, and you can optionally convert them to a nice PDF or using some LaTeX editor.

The first exam to be solved is the ITA (Instituto Tecnológico de Aeronáutica) exam for admissions in 2025, which is considered one of the most challenging exams in Brazil. This exam currently has two phases: the first one is a multiple choice test and a second one with a 4-hour essay test with 10 questions. The project will start by solving the second phase of the Math section, which is the essay test. This is particularly interesting because (i) the exam happened very recently on the 5th of November 2024 and (ii) the essay test requires a deep understanding of the subjects and the ability to write the answer step by step, which we'll evaluate as well.

After the first exam is solved, the project will try to solve the multiple choice test for Math and expand to other sections and eventually other exams. Feel free to contribute with ideas and implementations of other exams! 

Table of exams to be solved:

| Exam | Phase | Section | Type | Model | Status | Score |
|------|-------|---------|------|-------|--------|-------|
| ITA  | 2025  | Math    | Essay | o1-preview | 🚧 In Progress | - |

## How to use
So far, with just one exam, you just need to run `python src/resolve.py`. It will process a `exam_path` and it will save the results in the subfolder `solutions` as `.txt` files, one for each question. Make sure to set your env var `OPENAI_API_KEY` in the `.env` file. See section [Convert to LaTeX PDF](#convert-to-latex-pdf) to see how to convert the `.txt` files to a PDF.

## Convert to LaTeX PDF
🚧 In Progress...

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

## Sponsors

<p align="center">
  <a href="https://www.buser.com.br">
    <img src="assets/sponsors/buser-logo.png" alt="Buser Logo" width="100"/>
  </a>
</p>

This project is proudly sponsored by [Buser](https://www.buser.com.br), Brazil's leading bus travel platform.

