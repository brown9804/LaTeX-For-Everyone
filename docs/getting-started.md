---
pagetitle: Getting started with LaTeX
lang: en
---

# Getting started with LaTeX

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2026-11-18

[Home](index.md) |
[Edit on GitHub](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/docs/getting-started.md)

----------

> LaTeX separates a document's content from its typesetting. Write a `.tex`
> source file, compile it, and review the resulting PDF.

## Choose an editor

- **Browser:** use [Overleaf](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
  to create a blank project without installing a local TeX distribution.
- **Local:** install [TeX Live](https://www.tug.org/texlive/) or
  [MiKTeX](https://miktex.org/), then use a text editor. The commands below assume
  `pdflatex` is on your system's PATH.

Do not upload confidential material to an online editor without authorization.

## Your first document

Save this as `main.tex`:

```latex
\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{amsmath}

\title{My First LaTeX Document}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle

\section{Introduction}
\label{sec:introduction}
Hello, LaTeX! This is a reusable starting point for a short report.

\section{Results}
As introduced in Section~\ref{sec:introduction}, clear structure matters.
An example equation is
\begin{equation}
  E = mc^2.
  \label{eq:energy}
\end{equation}
Equation~\ref{eq:energy} has an automatically generated number.
\end{document}
```

In an online editor, select **Recompile**. Locally, run:

```shell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Open `main.pdf`. The second pass resolves cross-references. If compilation fails,
read the first error in `main.log`, fix it, and compile again.

## Mathematical notation

Inline math uses dollar signs: `$a^2 + b^2 = c^2$` produces $a^2 + b^2 = c^2$.

A display equation such as

$$
\int_0^1 x^2\,dx = \frac{1}{3}
$$

can be written in a `.tex` file with:

```latex
\[
  \int_0^1 x^2\,dx = \frac{1}{3}
\]
```

For aligned equations, load `amsmath` in the preamble and use:

```latex
\begin{align}
  f(x)  &= x^2 + 2x + 1, \\
  f'(x) &= 2x + 2.
\end{align}
```

## Academic writing

- Use `\section{...}` and `\subsection{...}` instead of manually numbering headings.
- Pair `\label{...}` with `\ref{...}` for references to sections and equations.
- Place a figure's `\label` after its `\caption`.
- Cite sources and follow your institution's or publisher's template.

For a small bibliography without an external database, insert this before
`\end{document}` in the article example:

```latex
For more background, see \cite{lamport1994}.

\begin{thebibliography}{9}
\bibitem{lamport1994}
Leslie Lamport.
\textit{LaTeX: A Document Preparation System}.
Addison-Wesley, second edition, 1994.
\end{thebibliography}
```

Compile twice to resolve the citation. For larger projects, consider
`biblatex` with Biber; follow the chosen template's build instructions.

## Presentations

Save this separate example as `slides.tex`:

```latex
\documentclass{beamer}
\usetheme{Madrid}
\title{My First Presentation}
\author{Your Name}
\date{\today}

\begin{document}
\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Key ideas}
  \begin{itemize}
    \item Separate content from presentation.
    \item Keep each slide focused.
    \item Use mathematics when it helps: $E = mc^2$.
  \end{itemize}
\end{frame}
\end{document}
```

Compile with `pdflatex -halt-on-error slides.tex` and open `slides.pdf`. Your TeX
distribution must include Beamer and its dependencies.

## Quick reference

| Task | LaTeX source |
| --- | --- |
| Bold | `\textbf{important}` |
| Italics | `\textit{emphasis}` |
| Section | `\section{Introduction}` |
| Fraction | `$\frac{a}{b}$` |
| Subscript / superscript | `$x_i^2$` |
| Bullet list | `\begin{itemize}\item First\end{itemize}` |
| Literal special characters | `\%`, `\&`, `\_`, `\#`, `\$` |
| Comment | `% This text is not typeset` |

## Common errors

| Symptom | What to check |
| --- | --- |
| Undefined control sequence | Check spelling and whether the required package is loaded. |
| Missing `$` inserted | Check math delimiters and escape underscores in ordinary text. |
| Reference displays `??` | Check the label name and compile again. |
| File not found | Check the filename, relative path, capitalization, and installed packages. |

[Return to the learning path](index.md)

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-0-limegreen" alt="Total repository views">
  <p>Refresh Date: 2026-11-18</p>
  <p>GitHub repository views, not website visits.</p>
</div>
<!-- END BADGE -->
