# Reusable templates

A template is a working starting point, not a document to submit unchanged.
Choose the class that matches your purpose, then check the destination's rules.

## Available templates

| Template | Main source | Requirements | Expected output |
| --- | --- | --- | --- |
| Article | [templates/article/main.tex](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/templates/article/main.tex) | pdfLaTeX, BibLaTeX, Biber | Short article with abstract, cross-reference, and bibliography |
| Thesis | [templates/thesis/main.tex](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/templates/thesis/main.tex) | pdfLaTeX, Biber, chapter files | Front matter, contents, chapters, appendix, and bibliography |
| Presentation | [templates/beamer/main.tex](https://github.com/brown9804/LaTeX-For-Everyone/blob/main/templates/beamer/main.tex) | pdfLaTeX, Beamer | Four-slide widescreen presentation |

The [article lesson](academic-writing.md), [thesis lesson](research-theses.md),
and [presentation lesson](presentations.md) display these exact sources and
explain the relevant commands.

## Use a template safely

1. Download or clone the full repository.
2. Read the corresponding lesson and compile the unmodified example first.
3. Keep the shared `resources/references.bib` path intact for the article and
   thesis, or copy that file into your own project and update `\addbibresource`.
4. Change the title, author, argument, data, and references deliberately.
5. Rebuild after small changes and inspect the resulting PDF.

For example, from the repository root:

```shell
cd templates/article
latexmk -pdf -outdir=build main.tex
```

Open `build/main.pdf`. If you copied the template outside the repository,
a missing `.bib` error indicates that you did not also adjust the bibliography.

## Adaptation checklist

- Is the document class accepted by your publisher or institution?
- Are margins, headings, citation style, and front matter appropriate?
- Have all teaching claims and author names been replaced with your own work?
- Are figures and borrowed materials licensed for your intended use?
- Have you checked accessibility and the final PDF, not only the source?

## Practice

Create a one-page reading summary with the article template or a four-slide
lesson with Beamer. Keep a note of each package you add and why it is necessary.

**Check:** the adapted document compiles from a clean folder and its instructions
list every required external file. See [troubleshooting](troubleshooting.md)
before copying packages from an unrelated template.
