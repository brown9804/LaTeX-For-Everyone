from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag in ("a", "link") and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in ("img", "script") and "src" in attrs:
            self.links.append(attrs["src"])


root = Path(__file__).resolve().parents[2]
site = root / "site"
prefix = "/LaTeX-For-Everyone/"
pages = {}
for path in site.rglob("*.html"):
    parser = Page()
    parser.feed(path.read_text(encoding="utf-8"))
    pages[path.resolve()] = parser
if not pages:
    raise SystemExit("The built website is missing.")

errors = []
for source, parser in pages.items():
    for link in parser.links:
        parts = urlsplit(link)
        if parts.scheme or parts.netloc:
            continue
        path = unquote(parts.path)
        if not path:
            target = source
        elif path.startswith(prefix):
            target = site / path[len(prefix):]
        elif path.startswith("/"):
            errors.append(f"{source.name}: link escapes repository site: {link}")
            continue
        else:
            target = source.parent / path
        if target.is_dir():
            target /= "index.html"
        target = target.resolve()
        if not target.is_file():
            errors.append(f"{source.name}: missing target {link}")
        elif parts.fragment and target in pages:
            if unquote(parts.fragment) not in pages[target].ids:
                errors.append(f"{source.name}: missing anchor {link}")

documentation = "\n".join(
    path.read_text(encoding="utf-8") for path in (root / "docs").rglob("*.md")
)
for folder in ("examples", "templates", "projects"):
    for source in (root / folder).rglob("main.tex"):
        if "build" not in source.relative_to(root).parts:
            if source.relative_to(root).as_posix() not in documentation:
                errors.append(f"Undocumented source: {source.relative_to(root)}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Checked internal links, fragments and assets across {len(pages)} HTML pages.")
