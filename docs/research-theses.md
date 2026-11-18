# Research papers, theses, and dissertations

**Prerequisites:** [academic writing](academic-writing.md) and
[bibliography management](bibliography.md).
**Goal:** organize a long document without losing a reproducible build.

## Start with the institution's rules

A thesis is not simply a longer article. Universities may prescribe front
matter, declarations, margins, line spacing, reference styles, accessibility,
and archival formats. Use an official template when one exists. The example
here teaches organization; it does not claim institutional approval.

For research papers, a venue's class and bibliography requirements take
precedence over the generic article template. Do not modify a publisher's class
to simulate compliance with an unrelated format.

## A multi-file thesis

[Complete source folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/templates/thesis).

```text
templates/thesis/
  main.tex
  chapters/
    introduction.tex
    method.tex
    conclusion.tex
```

```latex title="templates/thesis/main.tex"
--8<-- "templates/thesis/main.tex"
```

The `book` class provides `\frontmatter`, `\mainmatter`, and `\backmatter`.
These organize numbering and chapter behavior; they are not commands available
in every class. `\input` inserts a file's contents without creating a separate
document.

Here is the first chapter:

```latex title="templates/thesis/chapters/introduction.tex"
--8<-- "templates/thesis/chapters/introduction.tex"
```

The [method](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/templates/thesis/chapters/method.tex)
and [conclusion](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/templates/thesis/chapters/conclusion.tex)
complete the working example.

## Compile and expected output

From the repository root, with the shared bibliography still in place:

```shell
cd templates/thesis
latexmk -pdf -outdir=build main.tex
```

Open `build/main.pdf`. Expect a title page, an abstract, a table of contents,
three numbered chapters, an appendix with a reproducibility checklist, and a
bibliography. Chapter cross-references should resolve.
The appendix uses alphabetic numbering.

## Manage a growing project

- Keep one clear root document and compile it from its own directory.
- Name files after their purpose rather than their current chapter number.
- Use labels such as `chap:method` rather than `chapter2`.
- Commit sources, figures, data, and build instructions; keep disposable
  auxiliary files out of version control.
- For a large project, `\include` and `\includeonly` can support partial
  compilation, but `\include` introduces page breaks and auxiliary files.
  Understand that behavior before replacing `\input`.

## Practice

Add a chapter named `evaluation.tex`, include it before the conclusion, and
reference it from the introduction. Put it under version control.

**Check:** the contents page updates automatically, references remain correct
after reordering chapters, and another person can build from a clean checkout.

**Next:** [complete research workflow](projects/research-workflow.md).
