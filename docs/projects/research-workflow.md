# Project: a complete research writing workflow

**Prerequisites:** [academic writing](../academic-writing.md),
[bibliographies](../bibliography.md), and
[multi-file documents](../research-theses.md).
**Deliverable:** a small, reproducibly compiled manuscript with traceable sources
and an honest account of its limitations.

## Plan before formatting

This project uses a constructed checklist comparison to teach paper structure.
Its numbers are **invented for instruction**, not observations or evidence of
an intervention's effectiveness. Keeping that distinction visible is part of
the exercise.

The root file controls document settings; section files hold the argument;
the shared bibliography holds source metadata.

[Complete project folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/projects/research-paper).

```latex title="projects/research-paper/main.tex"
--8<-- "projects/research-paper/main.tex"
```

## Inspect the argument

```latex title="projects/research-paper/sections/introduction.tex"
--8<-- "projects/research-paper/sections/introduction.tex"
```

```latex title="projects/research-paper/sections/method-results.tex"
--8<-- "projects/research-paper/sections/method-results.tex"
```

```latex title="projects/research-paper/sections/discussion.tex"
--8<-- "projects/research-paper/sections/discussion.tex"
```

The table's caption and discussion both disclose the constructed data.
A formatted table is not, by itself, a research method.

## Compile and expected output

Preserve `resources/references.bib` in the repository:

```shell
cd projects/research-paper
latexmk -pdf -outdir=build main.tex
```

Open `build/main.pdf`. Expect an abstract, introduction, method, illustrative
results table, discussion, reproducibility statement, and bibliography.
The table reference resolves, and the citation to Lamport produces a
bibliography entry.

## Turn the demonstration into your own work

1. State an answerable research question.
2. Replace the constructed example with a justified method and appropriate
   evidence, or keep it explicitly framed as a conceptual argument.
3. Record data provenance and permissions. Do not publish sensitive research
   data merely to make a repository reproducible.
4. Cite checked sources and explain limitations.
5. Ask a reader to compile the project using only the supplied instructions.
6. Prepare a short talk using the [Beamer template](../presentations.md).

## Review exercise

Move the discussion before the results and rebuild. The document may still
compile correctly, but the argument may become harder to follow.
Restore the logical order and explain why it helps.

**Check:** distinguish three independent questions: does it compile, is it
clearly communicated, and are its claims justified? Only the first is directly
established by the automated LaTeX build.
