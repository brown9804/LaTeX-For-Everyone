# Tables, figures, and cross-references

**Prerequisite:** [fundamentals](fundamentals.md).
**Goal:** distinguish a float container from its contents and reference both.

## Understand floats

`table` and `figure` are floating containers: LaTeX can move them to improve
page layout. A `tabular` constructs rows and columns; it does not float by itself.
The placement hint `[htbp]` means here, top, bottom, or a float page. It is not
a promise of an exact position.

Put a `\label` after a float's `\caption`. That way it captures the caption's
counter, not the most recently numbered section.

## Complete example

This example draws its own diagram, so it needs no downloaded image.
[Source folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/examples/tables-figures).

```latex title="examples/tables-figures/main.tex"
--8<-- "examples/tables-figures/main.tex"
```

In `{llr}`, the first two columns are left-aligned and the last is right-aligned.
`&` separates cells; `\\` ends a row. `booktabs` provides rules with spacing
suited to a simple data table. Avoid dense vertical rules unless they are
genuinely needed for interpretation.

## Compile and expected output

```shell
cd examples/tables-figures
latexmk -pdf -outdir=build main.tex
```

From the repository root, enter that folder and open `build/main.pdf` afterward.
Expect a three-row table and a diagram containing **Write**, **Compile**, and
**Review** connected from left to right. The text should reference Table 1 and
Figure 1, even if a float moves.

## Include your own image

For a real image, load `graphicx` and replace the diagram with an inclusion
such as the following **fragment**, after adding your own `figures/result.pdf`:

```latex
\includegraphics[width=0.8\linewidth]{figures/result.pdf}
```

Use descriptive filenames and captions, confirm the image's license, and avoid
publishing personal or confidential information. PDF is convenient for vector
figures; PNG and JPEG can be appropriate for raster images with pdfLaTeX.

## Practice

Add a fourth table row and a return arrow from **Review** to **Write**.
Explain the feedback loop in the caption as well as visually.

**Check:** the table has the same number of `&` separators on each row,
references resolve, and the figure's meaning is understandable without color.

**Next:** [academic writing](academic-writing.md) or
[TikZ and PGFPlots](tikz-pgfplots.md).
