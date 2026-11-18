# Bibliography management

**Prerequisite:** [fundamentals](fundamentals.md).
**Goal:** maintain reusable references and understand the compilation sequence.

## Separate the three responsibilities

1. A `.bib` database stores citation metadata.
2. BibLaTeX controls citation and bibliography formatting in the document.
3. Biber processes the database and the document's citation requests.

BibLaTeX and BibTeX are not interchangeable names. This platform's examples
use **BibLaTeX with Biber**. A journal template using BibTeX may require a
different package and build sequence.

## The bibliography database

[Canonical shared database](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/resources/references.bib).
These entries describe external works; their full text is not distributed here.

```bibtex title="resources/references.bib"
--8<-- "resources/references.bib"
```

The key `lamport1994` is an identifier of our choosing. It must match the key
inside `\textcite{lamport1994}` or `\parencite{lamport1994}`.
Braces around `{LaTeX}` preserve its capitalization where a style changes titles.

## Complete example

[Source folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/examples/bibliography).

```latex title="examples/bibliography/main.tex"
--8<-- "examples/bibliography/main.tex"
```

`\textcite` makes the author part of the sentence; `\parencite` produces
a parenthetical citation. The exact punctuation comes from the chosen style.
`\printbibliography` normally lists cited entries, not every item in the database.

## Compile and expected output

Run from the repository root:

```shell
cd examples/bibliography
latexmk -pdf -outdir=build main.tex
```

Open `build/main.pdf`. Expect an author-in-text citation to Lamport, a
parenthetical reference to the LaTeX documentation, and two bibliography items.
The uncited PGFPlots entry should not appear.

Without `latexmk`, the sequence in this folder is:

```shell
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Biber takes the job name `main`, not `main.tex`. If a citation stays unresolved,
check its key, the `.bib` path, and the Biber log.

## Practice

Cite `pgfplots` in a new sentence about plotting documentation.
Rebuild and verify that the bibliography now includes that entry.
Change the style from `authoryear` to `numeric` and inspect the difference.

**Check:** no citation prints its raw key or an unresolved marker, and each
entry's metadata matches the actual source.

**Next:** [research papers and theses](research-theses.md).
