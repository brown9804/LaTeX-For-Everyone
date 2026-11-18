# LaTeX fundamentals

**Prerequisite:** [compile your first document](getting-started.md).
**Goal:** use semantic structure instead of manual spacing.

## Think in structure

An article is built from sections, paragraphs, lists, and references. A blank
line starts a new paragraph. A single line break usually behaves like a space.
Do not use repeated `\\` commands to create paragraph spacing; `\\` requests
a line break in contexts that support it.

- `\documentclass` selects the overall document type.
- `\usepackage` loads capabilities in the preamble.
- `\section` and `\subsection` express the document hierarchy.
- `\label` names a numbered object; `\ref` retrieves its number.
- `\newcommand` gives a repeated idea a meaningful name.

## Complete example

[Source and folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/examples/fundamentals).

```latex title="examples/fundamentals/main.tex"
--8<-- "examples/fundamentals/main.tex"
```

The empty group in `\toolname{}` keeps the following space from being swallowed
after a command name. `Section~\ref{...}` uses a non-breaking space so that the
word and its number stay together.

## Compile and inspect

From the repository root:

```shell
cd examples/fundamentals
latexmk -pdf -outdir=build main.tex
```

**Expected output:** a title, two sections, one subsection, an ordered plan,
a bullet list, a working external link, and the text **25%**.
The section reference resolves to the introduction.

Characters such as `%`, `&`, `_`, `#`, and `$` have special meanings.
In ordinary text use `\%`, `\&`, `\_`, `\#`, and `\$` when you need the
literal symbols. A `%` otherwise starts a comment through the end of the line.

## Practice

Add a third section with a label and refer to it from the introduction.
Change `\toolname` once and check that every use changes.
Insert `50% completed` and observe why the rest of that source line disappears;
repair it as `50\% completed`.

**Check your work:** the reference displays a number, the list numbering is
automatic, and no manual spaces are needed to align headings.

**Next:** [mathematics](mathematics.md).
