# Beamer presentations

**Prerequisite:** [fundamentals](fundamentals.md).
**Goal:** create a focused slide deck and understand frames.

## A frame is a unit of communication

Beamer is a document class for presentations. A `frame` usually produces one
slide, but overlays can produce multiple PDF pages from a single frame.
Begin without overlays so that the relationship between source and output is
easy to understand.

Keep one main idea per slide. A small font may make the PDF compile, but it does
not make dense content readable from the back of a room.

## Complete slide deck

[Source folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/templates/beamer).

```latex title="templates/beamer/main.tex"
--8<-- "templates/beamer/main.tex"
```

`aspectratio=169` requests a widescreen layout. The `Madrid` theme ships with
Beamer. A `block` groups a short idea with a heading; it is not a substitute for
an explanatory sentence.

## Compile and expected output

```shell
cd templates/beamer
latexmk -pdf -outdir=build main.tex
```

Start from the repository root and open `build/main.pdf` afterward.
Expect four slides: a title, a three-step workflow, a derivative example, and a
takeaway. The derivative of $x^2$ is $2x$, giving $2$ at $x=1$.

## Reveal information deliberately

For a small overlay experiment, insert `\pause` after the first `\item`.
Recompile. That frame now occupies additional PDF pages because information
is revealed in stages. Do not interpret the increased PDF page count as
additional source frames.

When presenting code, use a frame with the `fragile` option if it contains
verbatim material. For example, `\begin{frame}[fragile]{Code}` permits the
standard `verbatim` environment.

## Practice

Replace the mathematical slide with a diagram from
[TikZ and PGFPlots](tikz-pgfplots.md). Add a sentence explaining what the arrows
mean. Rehearse the transition from the previous slide.

**Check:** text remains legible at presentation distance, essential information
is not revealed only by color, and a reader can understand the PDF without
hearing your narration.

**Next:** [templates](templates.md) or [diagramming](tikz-pgfplots.md).
