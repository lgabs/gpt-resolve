# gpt-resolve
Can GPT solve Brazilian university entrance exams?

This project is an implementation of how to use LLMs to solve challenging Brazilian university entrance exams.

We'll use `o1-preview`, which is the best OpenAI model so far with reasoning capabilities, and `gpt-4o` to describe the exam images so that `o1-preview` can solve them on question at a time (as it does not have image capabilities yet). Results are saved as txt files with LaTeX formatting, and you can optionally convert them to a nice PDF or using some LaTeX editor.

The first exam to be solved is the ITA (Instituto Tecnológico de Aeronáutica) exam for admissions in 2025, which is considered one of the most challenging exams in Brazil. The project will start by solving the second phase of the Math section, which is the essay test. This is particularly interesting because (i) the exam happened very recently on the 5th of November 2024 and (ii) the essay test requires a deep understanding of the subjects and the ability to write the answer step by step, which we'll evaluate as well. See more details in the in-progress [report](exams/ita_2025/report.md).

After the first exam is solved, the project will try to solve the multiple choice test for Math and expand to other sections and eventually other exams. Feel free to contribute with ideas and implementations of other exams! 

Table of exams to be solved:

| Exam | Year | Model | Status | Score | Report |
|------|------|-------|--------|-------|--------|
| ITA  | 2025 | o1-preview | 🚧 In Progress | - | [Report](exams/ita_2025/report.md) |

### Installation and How to use

```bash
pip install gpt-resolve
```

`gpt-resolve` provides a simple CLI with two main commands: `resolve` for solving exam questions and `compile-solutions` for generating PDFs from the solutions. 

### Solve exams

To generate solutions for an exam:
- save the exam images in the exam folder `exam_path`, one question per image file
- run `gpt-resolve resolve -p exam_path` and grab a coffee while it runs.

See `gpt-resolve resolve --help` for more details about solving only a subset of questions or controlling token usage.


### Compile solutions into a single PDF

Once you have the solutions in your exam folder `exam_path`, you can compile them into a single PDF:
- run `gpt-resolve compile-solutions -p exam_path --title "Your Exam Title"`

For that command to work, you'll need a LaTeX distribution in your system. See some guidelines [here](https://www.tug.org/texlive/) (MacTeX for MacOS was used to start this project).

## Troubleshooting

Sometimes, it was observed that the output from `o1-preview` produced invalid LaTeX code when nesting display math environments (such as `\[...\]` and `\begin{align*} ... \end{align*}` together). The current prompt for `o1-preview` adds an instruction to avoid this, which works most of the time. If that happens, you can try to solve the question again by running `gpt-resolve resolve -p exam_path -q <question_number>`, or making more adjustments to the prompt, or fixing the output LaTeX code manually.

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

