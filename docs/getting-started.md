# Getting started with LaTeX

**Goal:** compile a small document, recognize its source structure, and resolve
a cross-reference. You only need basic text editing skills.

LaTeX is a typesetting system: you write a `.tex` file containing content and
commands, then compile it into a PDF. The source is not the final page layout.

## Choose an editor

=== "Browser"

    Start a blank project in [Overleaf](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes).
    Upload the source linked below or paste it into `main.tex`, choose
    **pdfLaTeX**, and select **Recompile**. Do not upload confidential documents
    without authorization.

=== "Local computer"

    Install [TeX Live](https://www.tug.org/texlive/) or
    [MiKTeX](https://miktex.org/) and an editor. Ensure `pdflatex`, `latexmk`,
    and, for later lessons, `biber` are available on your PATH.
    A minimal distribution may require additional packages.

    In a terminal, run `pdflatex --version` and `latexmk -v`. If either command
    is missing, fix the installation before editing a complex project.

## Get the learning resources

Download the repository's ZIP using **Code > Download ZIP**, or use Git:

```shell
git clone https://github.com/brown9804/LaTeX-For-Everyone.git
cd LaTeX-For-Everyone
```

Keep the directory structure intact. Later bibliography examples share
`resources/references.bib` and resolve it relative to their own folders.

## Your first document

[Open the complete source on GitHub](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/examples/hello-latex/main.tex).

```latex title="examples/hello-latex/main.tex"
--8<-- "examples/hello-latex/main.tex"
```

The **preamble** ends at `\begin{document}`. It selects a document class, loads
packages, and defines title information. The document body ends at
`\end{document}`. `amsmath` supplies mathematical environments; `fontenc`
selects a text-font encoding, not an input-file encoding.
`lmodern` selects scalable Latin Modern fonts.

### Compile

From the repository root:

```shell
cd examples/hello-latex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Open `build/main.pdf`. `latexmk` reruns LaTeX when references need another pass.
Without `latexmk`, run `pdflatex main.tex` twice and open `main.pdf`.
The online editor manages these passes automatically.

### Expected output

A title, an author, a date, two numbered sections, and a numbered equation.
The references should read **Section 1** and **Equation 1**, not `??`.
Page breaks and fonts can vary slightly across TeX distributions.

### Try it

Change the author, add a sentence to the introduction, and change the equation
to `a^2+b^2=c^2`. Recompile. The equation number should remain automatic.

!!! tip "Read the first error"
    If compilation fails, open the log and find the first error with a source
    line number. Fix it before interpreting the later messages, which may be
    consequences of the same mistake.

## Mathematical notation

Write inline math as `\(x^2\)` and display math in `\[...\]` or an equation
environment. Continue with [mathematics](mathematics.md) for alignment,
matrices, and units.

## Academic writing

Use structural commands rather than manually formatting every heading.
The [academic writing lesson](academic-writing.md) introduces an abstract,
citations, and a reusable article.

## Presentations

The [Beamer lesson](presentations.md) provides a complete slide deck rather
than treating presentation slides as small article pages.

## Quick reference

Use the [cheat sheet](cheat-sheet.md) when you remember an idea but not its
command. It distinguishes complete documents from fragments.

## Common errors

Missing commands usually indicate a typo or missing package. `??` usually
indicates an unresolved label or insufficient compilation passes.
See [troubleshooting](troubleshooting.md) for a step-by-step diagnosis.

**Next:** [fundamentals](fundamentals.md).
