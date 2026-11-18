# TikZ and PGFPlots

**Prerequisites:** [mathematics](mathematics.md) and
[tables and figures](tables-figures.md).
**Goal:** create an original vector diagram and a labelled function plot.

## Choose the right tool

TikZ describes shapes, nodes, and paths. PGFPlots builds on TikZ to provide axes,
coordinates, legends, and data plotting. A diagram communicates relationships;
a plot communicates quantitative relationships. Both need an explanation in
ordinary text.

## Complete example

[Source folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/examples/tikz-pgfplots).

```latex title="examples/tikz-pgfplots/main.tex"
--8<-- "examples/tikz-pgfplots/main.tex"
```

The `positioning` library enables `right=of source`.
`arrows.meta` provides configurable arrow tips.
A named style such as `process node/.style={...}` keeps related nodes consistent
without reusing TikZ's existing `step` key.

For the plot, `compat=1.18` requests a documented PGFPlots behavior level.
It is not a package version installer. Use a distribution containing that
compatibility level or consult your installed manual.

## Compile and expected output

```shell
cd examples/tikz-pgfplots
latexmk -pdf -outdir=build main.tex
```

From the repository root, enter that folder and open `build/main.pdf`.
Expect a **Source ? Build ? PDF** diagram and a plot of $x^2$ and $x$ on
$0\leq x\leq2$. They intersect at $x=0$ and $x=1$.
The dashed line remains distinguishable from the solid curve in grayscale.

## Plot data without rewriting it

For measured or tabulated data, prefer a CSV file to copying points into
several places. The [laboratory report](projects/lab-report.md) reads one CSV
for both its table and its plotted points. Label the axes with quantities and
units, and explain whether values are observed, simulated, or synthetic.

Large plots can slow compilation. Simplify a problematic example first.
TikZ externalization is an advanced optimization that may require shell-escape;
none of this platform's examples needs unrestricted shell execution.

## Practice

Change the plot domain to `-1:2`. Predict the behavior before compiling:
$x^2$ stays nonnegative while $x$ becomes negative to the left of zero.
Move the PDF node below the Build node and reroute the arrow.

**Check:** axis labels, legend entries, and explanatory text still match the
new graph. The diagram does not rely on arrow color alone.

**Next:** [laboratory report project](projects/lab-report.md).
