# LaTeX cheat sheet

These are **fragments**, not complete documents. Put them into an appropriate
document body unless the table says preamble. Start from a
[working template](templates.md) if you need a complete example.

## Structure and text

| Task | Source | Note |
| --- | --- | --- |
| Document class | `\documentclass{article}` | Preamble, first command |
| Load package | `\usepackage{amsmath}` | Preamble |
| Heading | `\section{Introduction}` | Numbering is automatic |
| Emphasis | `\emph{important}` | Semantic emphasis |
| Bold | `\textbf{important}` | Font weight |
| New paragraph | Blank source line | Not repeated `\\` |
| Comment | `% explanation` | Rest of line is ignored |
| Literal symbols | `\% \& \_ \# \$` | Ordinary text |
| Non-breaking space | `Section~\ref{sec:intro}` | Keeps word and number together |
| Named command | `\newcommand{\term}{LaTeX}` | Usually in preamble |

## Mathematics

| Task | Source | Package |
| --- | --- | --- |
| Inline | `\(x_i^2\)` | Core LaTeX |
| Display | `\[a+b=c\]` | Core LaTeX |
| Fraction | `\frac{a}{b}` | Math mode |
| Root | `\sqrt{x}` | Math mode |
| Summation | `\sum_{i=1}^{n} x_i` | Math mode |
| Real numbers | `\mathbb{R}` | `amssymb` |
| Matrix | `\begin{bmatrix}1&0\\0&1\end{bmatrix}` | `amsmath` |
| Quantity | `\qty{2}{\metre\per\second}` | `siunitx` v3 |

See the [mathematics lesson](mathematics.md) for environments and expected output.

## References and citations

| Task | Source |
| --- | --- |
| Name a section | `\label{sec:intro}` after its heading |
| Refer to it | `\ref{sec:intro}` |
| Name a figure | `\label{fig:result}` after its caption |
| Parenthetical citation | `\parencite{lamport1994}` with BibLaTeX |
| Author-in-text citation | `\textcite{lamport1994}` with BibLaTeX |
| Print cited bibliography | `\printbibliography` |

## Build commands

Run inside a folder containing a root `main.tex`:

```shell
latexmk -pdf -outdir=build main.tex
```

Expected output: `build/main.pdf`. To inspect errors, read `build/main.log`.
For Biber-based documents without `latexmk`, use
`pdflatex main.tex`, `biber main`, then two more `pdflatex main.tex` passes.

**Quick exercise:** identify the preamble-only commands in this page before
copying a fragment into your document. If an error appears, use
[troubleshooting](troubleshooting.md), not a random list of extra packages.
