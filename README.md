# LaTeX for Everyone: <br> Learning Path - Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)
[![Validation and Pages](https://github.com/brown9804/LaTeX-For-Everyone/actions/workflows/md-html-deploy.yml/badge.svg)](https://github.com/brown9804/LaTeX-For-Everyone/actions/workflows/md-html-deploy.yml)

Last updated: 2026-11-18

----------

An open-source, beginner-friendly LaTeX learning platform connecting original
Markdown lessons with working source files, reusable templates, and complete
projects. Built for students, researchers, educators, and professionals.

[Read the website](https://brown9804.github.io/LaTeX-For-Everyone/) |
[Start learning](docs/getting-started.md) |
[Choose a learning path](docs/learning-paths.md) |
[Contribute](CONTRIBUTING.md)

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Learning resources](#learning-resources)
- [Repository structure](#repository-structure)
- [Compile an example](#compile-an-example)
- [Website and validation](#website-and-validation)
- [Repository views counter](#repository-views-counter)
- [Community and license](#community-and-license)

</details>

## Learning resources

| Topic | Lesson |
| --- | --- |
| First document and fundamentals | [Getting started](docs/getting-started.md), [fundamentals](docs/fundamentals.md) |
| Mathematical notation | [Equations, matrices, and units](docs/mathematics.md) |
| Tables and figures | [Floats, captions, and references](docs/tables-figures.md) |
| Academic writing | [Scientific article structure](docs/academic-writing.md) |
| Research and theses | [Multi-file papers, theses, and dissertations](docs/research-theses.md) |
| Bibliographies | [BibLaTeX and Biber](docs/bibliography.md) |
| Presentations | [Beamer](docs/presentations.md) |
| Diagrams and plots | [TikZ and PGFPlots](docs/tikz-pgfplots.md) |
| Reusable starting points | [Article, thesis, and slide templates](docs/templates.md) |
| Practical projects | [Laboratory report](docs/projects/lab-report.md), [research workflow](docs/projects/research-workflow.md) |
| Reference | [Cheat sheet](docs/cheat-sheet.md), [troubleshooting](docs/troubleshooting.md), [official resources](docs/resources.md) |

## Repository structure

```text
docs/                  Markdown lessons and Material theme overrides
examples/              Focused, standalone LaTeX examples
templates/             Reusable article, thesis, and Beamer sources
projects/              Complete projects with supporting data and section files
resources/             Shared bibliography metadata
.github/               Validation, deployment, counter automation, and issue forms
mkdocs.yml             Website navigation and configuration
requirements-docs.txt  Documentation dependencies
```

The website includes canonical `.tex` files directly from these folders.
Source links beside each embedded example also make it usable when reading
the Markdown on GitHub. Do not maintain a second pasted source copy.

## Compile an example

Install a current TeX distribution with `latexmk` and Biber. Clone or download
the repository, keep its structure, and run:

```shell
cd examples/hello-latex
latexmk -pdf -outdir=build main.tex
```

Open `build/main.pdf`. The [getting-started guide](docs/getting-started.md)
explains installation, expected output, and manual compilation passes.
Some examples use the shared `resources/references.bib`; preserve that relative
path or update it when copying a template into a separate project.

## Website and validation

The website uses **MkDocs Material** with light (default) and dark themes,
search, responsive navigation, breadcrumbs, syntax highlighting, copy-code
buttons, GitHub source links, and MathJax.

In an activated Python 3.12 environment:

```shell
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

See the [maintenance guide](docs/community/maintaining.md) for the full toolchain
and validation commands. GitHub Actions performs:

1. Focused automation tests.
2. A strict MkDocs build and generated internal-link checks.
3. Compilation of all standalone `main.tex` resources with `latexmk`.
4. PDF and log artifact upload.
5. GitHub Pages deployment, only after successful validation on `main`.

The workflow filename `md-html-deploy.yml` and existing
`getting-started.html` URL are retained. The older Pandoc implementation is
replaced because the platform now requires MkDocs Material.
Generated site files and LaTeX build outputs are not committed.

## Repository views counter

The reference-style badge below reports accumulated **GitHub repository
views**, including repeat visits, not GitHub Pages traffic or unique people.
The [counter workflow](.github/workflows/use-visitor-counter.yml) merges daily
traffic into [metrics.json](metrics.json), updates this README and the shared
website footer, and requests a fresh Pages build.

For automatic refresh, create a fine-grained token restricted to this repository
with **Administration: read** permission and save it as the `TRAFFIC_TOKEN`
Actions secret. Then manually run **Update repository views** once.
Never commit a token or paste one into an issue.

Without that secret, the workflow explicitly warns and preserves the last
confirmed count. History begins with the initial available traffic window;
gaps longer than 14 days can leave missing history.

## Community and license

Use the [contribution guide](CONTRIBUTING.md), [code of conduct](CODE_OF_CONDUCT.md),
and [issue forms](https://github.com/brown9804/LaTeX-For-Everyone/issues/new/choose).
Corrections, beginner feedback, tested examples, and focused lesson proposals
are welcome.

Original project content follows the existing [license](LICENSE). External
resources keep their own licenses; no third-party manuals or proprietary
templates are redistributed. The initial identity and counter presentation
were inspired by
[Cloud-DevOps-Overview](https://github.com/brown9804/Cloud-DevOps-Overview).

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-0-limegreen" alt="Total repository views">
  <p>Refresh Date: 2026-11-18</p>
  <p>GitHub repository views, not website visits.</p>
</div>
<!-- END BADGE -->
