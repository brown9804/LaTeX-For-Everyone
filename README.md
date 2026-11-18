# LaTeX for Everyone: <br> Learning Path - Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2026-11-18

----------

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
- [Repository views counter](#repository-views-counter)

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
its own LaTeX-focused documentation. Cloud-specific integration tests are not
copied.

The site build validates Markdown-to-HTML generation, not LaTeX compilation.
Follow the compilation steps in the examples to produce PDFs.

## Repository views counter

Like the reference repository, the badge below displays accumulated **GitHub
repository views**, including repeat views, with a refresh date. It does not
count visits to the GitHub Pages website or represent unique people.

The [counter workflow](.github/workflows/use-visitor-counter.yml) runs daily and
can also be run manually. It merges GitHub's last 14 days of traffic into
[`metrics.json`](metrics.json), replacing overlapping dates rather than counting
them twice, and updates the README and documentation badges.
History begins with the initial available traffic window; older visits cannot
be recovered. Gaps longer than 14 days can leave missing history.

To enable automatic refresh:

1. Create a fine-grained token restricted to this repository with
   **Administration: read** permission, required by GitHub's repository traffic
   API. Do not paste the token into a file or issue.
2. Save it as **Settings > Secrets and variables > Actions > New repository
   secret > `TRAFFIC_TOKEN`**.
3. Run **Actions > Update repository views > Run workflow**.

Without this secret, the workflow reports a warning and leaves the last
confirmed count and refresh date unchanged. Writes use the workflow's
`GITHUB_TOKEN`, not the traffic token. A successful update also requests a fresh
Pages build so the website badges stay in sync.

## Contributing

Issues and pull requests are welcome. Keep examples minimal, identify required
packages and compilation commands, and never submit confidential documents.

## License

See [LICENSE](LICENSE).

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-0-limegreen" alt="Total repository views">
  <p>Refresh Date: 2026-11-18</p>
  <p>GitHub repository views, not website visits.</p>
</div>
<!-- END BADGE -->
