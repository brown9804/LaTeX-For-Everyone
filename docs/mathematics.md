# Mathematics and equations

**Prerequisite:** [fundamentals](fundamentals.md).
**Goal:** choose appropriate math environments and write readable notation.

## Choose an environment

| Purpose | In a `.tex` source |
| --- | --- |
| Inline expression | `\(f(x)=x^2\)` |
| Unnumbered display | `\[f(x)=x^2\]` |
| Numbered display | `\begin{equation}...\end{equation}` |
| Aligned derivation | `\begin{align}...\end{align}` |

In this Markdown website, dollar delimiters are processed by MathJax.
For example, $\int_0^1 x^2\,\mathrm{d}x=\frac{1}{3}$.
The `.tex` sources use LaTeX's own environments; MathJax is not the PDF compiler.

## Complete example

[Source folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/examples/mathematics).

```latex title="examples/mathematics/main.tex"
--8<-- "examples/mathematics/main.tex"
```

`amsmath` provides `align`, `bmatrix`, and `cases`; `amssymb` supplies
additional symbols such as `\mathbb`. In `align`, `&` marks the alignment point,
not a visible symbol. `\\` ends an alignment row.

The command `\mathrm{d}` typesets an upright differential. The spacing command
`\,` separates it from the integrand. `siunitx` keeps quantities and units
consistent; the example uses the version 3 command `\qty`.

## Compile and expected output

```shell
cd examples/mathematics
latexmk -pdf -outdir=build main.tex
```

Run this from the repository root. Open `build/main.pdf`.
Expect a numbered derivative, an aligned two-line integral evaluation, a
two-by-two matrix, a piecewise function, and a speed with formatted units.
The displayed integral equals $1/3$; $f'(1)=4$.

!!! warning "Do not nest display environments"
    Do not put an `equation` environment inside `\[...\]` or wrap `align`
    in another math environment. Use `aligned` inside an existing display
    if you need a grouped alignment.

## Practice

Replace the model with $f(x)=x^3$ and update its derivative to $3x^2$.
Add a label to one aligned row and refer to it in a sentence.
Use `\notag` on a row you do not want numbered.

**Check:** the mathematics remains correct, the reference resolves, and the
alignment uses `&` rather than a run of spaces.

**Next:** [tables and figures](tables-figures.md).
