# Maintaining the platform

The repository is the source of truth. Markdown lessons live in `docs/`;
standalone LaTeX documents live in `examples/`, `templates/`, and `projects/`.
The website includes those sources directly using PyMdown Snippets. Do not
maintain a second pasted copy of a complete example.

## Repository map

| Location | Responsibility |
| --- | --- |
| `mkdocs.yml` | Site identity, navigation, themes, Markdown extensions |
| `requirements-docs.txt` | Pinned MkDocs and Material versions |
| `docs/` | Lessons, reference pages, community documentation |
| `docs/overrides/` | Shared breadcrumbs and repository counter footer |
| `docs/javascripts/mathjax.js` | MathJax setup and instant-navigation rendering |
| `examples/` | Small, focused compilable examples |
| `templates/` | Reusable article, thesis, and Beamer sources |
| `projects/` | Complete learning projects and their data |
| `resources/references.bib` | Shared bibliography metadata |
| `.github/scripts/` | Link, source-coverage, compilation, and counter checks |
| `.github/workflows/` | Validation, Pages deployment, and counter updates |

## Local setup

Use Python 3.12 and a current TeX Live or MiKTeX installation containing
`latexmk`, Biber, `amsmath`, `siunitx` v3, BibLaTeX, Beamer, TikZ, PGFPlots,
`booktabs`, `geometry`, `lmodern`, and `microtype`.

Create a Python virtual environment from the repository root:

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements-docs.txt
    ```

=== "Linux or macOS"

    ```shell
    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r requirements-docs.txt
    ```

On Debian/Ubuntu, the CI toolchain uses `latexmk`, `biber`, `lmodern`,
`texlive-bibtex-extra`, `texlive-latex-extra`, `texlive-science`, `texlive-pictures`, and
`texlive-fonts-recommended`. Package names differ on other operating systems.

Preview the website:

```shell
python -m mkdocs serve
```

Open the localhost URL printed by MkDocs. Search, navigation, themes, and
MathJax should work. MathJax and the view badge require access to their public
CDNs; all LaTeX sources and ordinary site navigation are stored in the repository.

## Required validation

Run these commands from the repository root:

```shell
python -m unittest discover -s .github/scripts -p "test_*.py"
python -m mkdocs build --strict
python .github/scripts/check_site.py
python .github/scripts/validate_examples.py
```

- Strict MkDocs treats configuration and documentation warnings as failures.
- The site checker validates generated local links, fragment identifiers,
  stylesheets, scripts, and images. It also checks that every standalone
  `main.tex` appears in the documentation.
- The compilation checker discovers every standalone `main.tex`, runs
  `latexmk` from its own folder, verifies a PDF was produced, and rejects
  unresolved citations or references.
- Counter tests cover overlapping traffic windows, invalid history, and
  updates to the shared footer without altering lesson text.

The checks do not crawl external websites or certify PDF accessibility.
Preview mobile navigation, keyboard focus, both themes, search, equations,
and affected PDFs before declaring a change ready.

## Deployment

The existing workflow filename
`md-html-deploy.yml` is retained so manual dispatches and the counter's rebuild
step keep working. Its implementation now uses **MkDocs Material**, not Pandoc.

Pushes to `main` and pull requests run the same validations. Only a successful
`main` run deploys using GitHub Pages. A manual run on a non-main branch
validates without publishing. Set **Settings > Pages > Source** to
**GitHub Actions**.

`site_url` includes `/LaTeX-For-Everyone/`, and `use_directory_urls: false`
retains existing URLs such as `getting-started.html`. Generated HTML stays in
the Pages artifact rather than being committed. Each run also uploads
compiled PDFs and logs as **latex-examples**.

## Repository views counter

The badge counts accumulated GitHub **repository views**, including repeat
views. It is not website analytics or a unique-person count. GitHub only
exposes a recent traffic window; the tracked `metrics.json` stores daily
history, and overlapping days are replaced rather than added twice.
Gaps longer than 14 days can leave unrecoverable history.

Automatic refresh requires a fine-grained `TRAFFIC_TOKEN` restricted to this
repository with **Administration: read** permission. Add it under
**Settings > Secrets and variables > Actions**, then run
**Update repository views**. Do not put credentials in any source file.

If the secret is missing, the workflow reports a warning and leaves the last
confirmed badge unchanged. Repository writes and the subsequent Pages rebuild
use `GITHUB_TOKEN`. The counter updates only the README, shared footer, and
metrics; new lessons do not need individual badge blocks.

## Dependency and content maintenance

Keep dependency updates separate from unrelated lessons and rerun the full
validation pipeline. Preserve existing links when moving a page. Review
copyright and attribution for every external asset; do not copy manuals.

The original repository license remains unchanged. The reference
[Cloud-DevOps-Overview](https://github.com/brown9804/Cloud-DevOps-Overview)
inspired the initial identity and counter presentation; this platform now uses
its own MkDocs architecture and original LaTeX teaching material.
