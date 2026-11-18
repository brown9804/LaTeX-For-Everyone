# Academic and scientific writing

**Prerequisite:** [fundamentals](fundamentals.md) and
[bibliography basics](bibliography.md).
**Goal:** produce a structured, traceable academic article.

## Structure follows the argument

A title identifies the work; an abstract summarizes its purpose and limits.
The introduction states the problem. Methods explain what was actually done,
results report observations, and discussion interprets them. Not every field
uses the same section names, so follow the venue's requirements.

The reusable article below is a short conceptual teaching document, not a
fabricated empirical study. Notice that it explicitly separates a successful
compilation from a scientifically justified claim.

## Complete article

[Source folder](https://github.com/brown9804/LaTeX-For-Everyone/tree/main/templates/article).
It shares the [bibliography](bibliography.md#the-bibliography-database)
with other repository examples.

```latex title="templates/article/main.tex"
--8<-- "templates/article/main.tex"
```

`geometry` controls margins; `microtype` refines typography.
`lmodern` supplies scalable fonts suitable for pdfLaTeX font expansion.
`hyperref` makes references and URLs navigable. These are helpful defaults,
not a replacement for a publisher's document class.

## Compile and expected output

Keep the full repository structure:

```shell
cd templates/article
latexmk -pdf -outdir=build main.tex
```

`latexmk` calls Biber when the bibliography requires it.
Open `build/main.pdf`. Expect a title, an abstract, four sections, a resolved
section reference, an author-year citation, and a bibliography.

## Cite accurately

Use sources you have actually checked. A bibliography entry records metadata;
it does not license copying the source's text or images. Mark quotations
clearly, cite ideas and data appropriately, and follow the relevant style guide.
Do not use a citation merely because it appears in this teaching template.

## Accessibility and review

- Use real section commands and a logical heading hierarchy.
- Give figures descriptive captions and explain essential information in text.
- Do not encode differences by color alone.
- Check reading order, link meaning, table structure, and contrast in the PDF.
- Follow current [LaTeX tagged-PDF guidance](https://latex3.github.io/tagging-project/)
  and your institution's requirements when accessible PDF output is required.

These examples are **not certified PDF/UA-conformant documents**. Package
support and tagging workflows continue to evolve; inspect the actual output
with appropriate assistive technology and validation tools.

## Practice

Replace the conceptual argument with a one-page literature summary.
Add a clear limitation and a citation supporting one specific statement.

**Check:** a reader can identify which statement each citation supports,
distinguish claims from evidence, and find the cited work.

**Next:** [research papers and theses](research-theses.md).
