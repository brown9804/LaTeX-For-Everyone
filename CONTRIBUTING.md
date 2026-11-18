# Contributing

Thank you for helping make LaTeX easier to learn. Contributions can improve
explanations, fix reproducible problems, extend working examples, or introduce
a carefully scoped tutorial.

## Before you start

1. Read the [code of conduct](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/CODE_OF_CONDUCT.md).
2. Search existing issues and check the current learning path.
3. For a substantial new topic or architectural change, open a lesson proposal
   before implementing it.
4. Work on a focused branch and submit a pull request against `main`.

## Educational contribution checklist

- State the learner's goal and prerequisites.
- Explain the relevant concepts, not just the commands.
- Provide a complete, compilable `main.tex` in `examples/`, `templates/`, or
  `projects/`, with any required data or supporting files.
- Include the real source in its lesson using the existing Snippets extension.
  Link to the GitHub source so readers can find it outside the website.
- Give the compilation command, expected output, and a checkable exercise.
- Update navigation and link to the lesson from a relevant learning path.
- Identify synthetic data and separate demonstration claims from real findings.
- Use original material, or verify license compatibility and attribution.

Use kebab-case folder and Markdown filenames. Standalone LaTeX documents use
`main.tex`; chapter and section fragments must not add another
`\documentclass`. Add packages only when the example requires them.

## Validate your change

The [maintenance guide](https://brown9804.github.io/LaTeX-For-Everyone/community/maintaining.html)
lists the full setup and commands. Before submitting, run:

```shell
python -m unittest discover -s .github/scripts -p "test_*.py"
python -m mkdocs build --strict
python .github/scripts/check_site.py
python .github/scripts/validate_examples.py
```

Inspect the affected PDFs and website pages too. Automated checks cannot
establish that a scientific explanation is true or that a document meets a
specific accessibility or submission standard.

## Report a problem

Use a bug report for a reproducible failure and a lesson proposal for a new
topic. Include the relevant source path, command, tool versions, and first
useful error message. Never include credentials, private research, personal
information, or confidential documents.

Contributions are made under this repository's existing license. External
materials retain their own licenses; do not copy a manual or a proprietary
template into a pull request.
