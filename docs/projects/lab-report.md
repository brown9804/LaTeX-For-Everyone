# Project: a reproducible laboratory report

**Prerequisites:** [tables and figures](../tables-figures.md),
[mathematics](../mathematics.md), and optionally
[PGFPlots](../tikz-pgfplots.md).
**Deliverable:** a report whose table and plot use the same CSV data.

## The question

Can a small set of positions be described approximately by constant-speed
motion? We use **synthetic teaching data**, not measurements from a real
experiment. The aim is a reproducible document workflow, not an experimental
claim.

## Inspect the data

[Complete project folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/projects/lab-report).

```text title="projects/lab-report/measurements.csv"
--8<-- "projects/lab-report/measurements.csv"
```

The first row contains column names. Time is in seconds; position is in metres.
Keeping the data outside the document prevents the table and graph from
drifting apart when a value changes.

## Build the report

```latex title="projects/lab-report/main.tex"
--8<-- "projects/lab-report/main.tex"
```

`pgfplotstabletypeset` reads the CSV into a formatted table.
The `table[x=time,y=position,...]` expression reads the same data for the plot.
The dashed reference line is a mathematical model, not an extra observation.

From the repository root:

```shell
cd projects/lab-report
latexmk -pdf -outdir=build main.tex
```

Open `build/main.pdf`.

## Expected output and interpretation

The PDF contains an abstract, a question and method, a four-row table, a plot,
an endpoint calculation, a limitations paragraph, and a conclusion.
The point at time $2$ is at position $4.1$.

The endpoint estimate is

$$
v_{\mathrm{avg}}=\frac{6.0-0.0}{3-0}=2.0\ \mathrm{m\,s^{-1}}.
$$

That is an average over the interval. It does not show that the instantaneous
speed was exactly constant. A real report would explain instrumentation,
uncertainty, sampling, and whether the model is justified.

## Extension exercise

Change the position at time $2$ from `4.1` to `4.4`. Recompile without editing
the `.tex` file.

**Expected change:** both the table entry and plotted point move to `4.4`.
The endpoint average stays $2.0\ \mathrm{m\,s^{-1}}$ because the endpoints did
not change. The reference line also stays unchanged.

## Submission checklist

- The CSV and source are included.
- The table, plot, caption, and text agree.
- Synthetic data is explicitly labelled.
- References to the table and figure resolve.
- The build command works from a clean checkout.

**Next project:** [a research writing workflow](research-workflow.md).
