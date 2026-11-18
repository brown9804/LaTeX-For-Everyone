# Troubleshooting

Start with the first error, not the last page of the log. Many later messages
are consequences of a missing brace, delimiter, file, or package.

## A repeatable diagnosis

1. Save all edited files.
2. Check that the terminal is in the root document's folder.
3. Run `latexmk -pdf -halt-on-error -file-line-error -outdir=build main.tex`.
4. Open `build/main.log` and find the first source error.
5. Reduce the example until the failing feature is isolated.
6. Recompile after one deliberate fix.

**Expected result:** either a valid `build/main.pdf` or a smaller, clearer
failure that another person can reproduce.

## Common failures

| Symptom | Likely explanation | What to check |
| --- | --- | --- |
| `Undefined control sequence` | Typo or missing package | Exact spelling and the package's manual |
| `Missing $ inserted` | Math syntax in text or unmatched math delimiter | `_`, `^`, and math environment boundaries |
| `File ... not found` | Wrong path or missing dependency | Working directory, filename case, installed packages |
| `??` for a reference | Wrong label or incomplete passes | `\label`, `\ref`, and final build log |
| Citation key displayed | Biber did not complete or key is wrong | `.bib` path, key, backend, and `.blg` log |
| `Extra alignment tab` | Too many table or alignment separators | Column count and `&` characters |
| `Runaway argument` | Often an unclosed brace | The preceding command, not only the reported line |
| `Overfull \hbox` | Content exceeds a line | Long URLs, unbreakable text, wide tables |
| `\qty` is undefined | Old `siunitx` or package not loaded | `siunitx` version 3 and preamble |

An overfull-box warning is not normally a fatal error, but it can indicate
visibly clipped or overflowing content. Inspect the PDF rather than ignoring it.

## A useful minimal example

This document should compile with a standard LaTeX installation:

```latex
\documentclass{article}
\begin{document}
Hello.
\end{document}
```

Save it as `main.tex` in a new scratch folder and run `pdflatex main.tex`.
Expect a PDF containing **Hello.** Add only the package and content required
to reproduce your problem.

## Bibliography paths in this repository

The article, thesis, bibliography lesson, and research paper expect
`../../resources/references.bib` relative to their own folders. Compile from
those folders and keep the repository structure intact.
If you make a standalone copy, copy the database too and update the path.

## Stale output versus source problems

An old PDF can remain after a failed compilation. Check the log and output
timestamp before assuming your edit compiled. If auxiliary files are stale,
move only the affected example's `build` folder aside, then rebuild.
Do not delete source files or the shared bibliography.

## Ask for help responsibly

Open a [bug report](https://github.com/brown9804/LaTeX-For-Everyone/issues/new/choose)
with the failing source path, command, TeX distribution/version, and first
relevant error. Include a minimal example; remove personal details, unpublished
research, credentials, and confidential documents.
