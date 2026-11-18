import re
import subprocess
from pathlib import Path


root = Path(__file__).resolve().parents[2]
documents = sorted(
    path
    for folder in ("examples", "templates", "projects")
    for path in (root / folder).rglob("main.tex")
    if "build" not in path.relative_to(root).parts
)
if not documents:
    raise SystemExit("No compilable LaTeX documents found.")

failures = []
for source in documents:
    print(f"Compiling {source.relative_to(root)}", flush=True)
    result = subprocess.run(
        [
            "latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
            "-file-line-error", "-outdir=build", "main.tex",
        ],
        cwd=source.parent,
        check=False,
        timeout=180,
    )
    if result.returncode:
        failures.append(str(source.relative_to(root)))
        continue
    output = source.parent / "build"
    if not (output / "main.pdf").read_bytes().startswith(b"%PDF-"):
        raise SystemExit(f"Missing or invalid PDF for {source}")
    log = (output / "main.log").read_text(encoding="utf-8", errors="replace")
    if re.search(r"(undefined references|undefined citations|Citation .* undefined)", log):
        raise SystemExit(f"Unresolved references or citations in {source}")

if failures:
    raise SystemExit("Compilation failed for:\n" + "\n".join(failures))
print(f"Verified {len(documents)} compiled PDF documents.")
