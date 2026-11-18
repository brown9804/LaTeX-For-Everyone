# LaTeX-For-Everyone

A practical, beginner-friendly LaTeX knowledge hub featuring tutorials,
mathematical notation, academic writing examples, reusable templates,
presentations, cheat sheets, and real-world projects. Helping students,
researchers, educators, and professionals master LaTeX.

[Read the documentation](https://brown9804.github.io/LaTeX-For-Everyone/) |
[Browse the learning path](docs/index.md) |
[Getting started](docs/getting-started.md)

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Learning path](docs/index.md)
- [First document](docs/getting-started.md#your-first-document)
- [Mathematical notation](docs/getting-started.md#mathematical-notation)
- [Academic writing](docs/getting-started.md#academic-writing)
- [Presentations](docs/getting-started.md#presentations)
- [Quick reference](docs/getting-started.md#quick-reference)
- [Documentation publishing](#documentation-publishing)

</details>

## Documentation publishing

Learning content lives in [`docs/`](docs/). The
[GitHub Actions workflow](.github/workflows/md-html-deploy.yml) uses Pandoc to
build HTML, a table of contents, syntax highlighting, and MathJax equations.
Relative Markdown links are converted to HTML links for the published site.

- Pull requests to `main` build the site without deploying it.
- Pushes to `main` build and deploy to GitHub Pages.
- A manual run is available from the repository's **Actions** tab.
- In **Settings > Pages > Build and deployment**, the source must be
  **GitHub Actions**.
- Generated HTML is uploaded as a deployment artifact, not committed to `main`.

The layout and publishing approach are based on
[Cloud-DevOps-Overview](https://github.com/brown9804/Cloud-DevOps-Overview).
That reference currently has no `docs/` directory, so this repository provides
its own LaTeX-focused documentation. Cloud-specific integration tests and
secret-dependent visitor counters are intentionally not copied.

The site build validates Markdown-to-HTML generation, not LaTeX compilation.
Follow the compilation steps in the examples to produce PDFs.

## Contributing

Issues and pull requests are welcome. Keep examples minimal, identify required
packages and compilation commands, and never submit confidential documents.

## License

See [LICENSE](LICENSE).
