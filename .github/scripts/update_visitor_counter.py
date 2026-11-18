import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path


BADGE = re.compile(r"<!-- START BADGE -->.*?<!-- END BADGE -->", re.DOTALL)


def validate_entries(entries):
    if not isinstance(entries, list):
        raise ValueError("Traffic history must be a list.")
    dates = set()
    for entry in entries:
        day = entry["date"]
        if date.fromisoformat(day).isoformat() != day or day in dates:
            raise ValueError("Traffic dates must be unique ISO dates.")
        dates.add(day)
        for field in ("count", "uniques"):
            if type(entry[field]) is not int or entry[field] < 0:
                raise ValueError("Traffic counts must be non-negative integers.")
        if entry["uniques"] > entry["count"]:
            raise ValueError("Unique views cannot exceed total views.")
    return entries


def merge_metrics(existing, views):
    fetched = [
        {
            "date": item["timestamp"][:10],
            "count": item["count"],
            "uniques": item["uniques"],
        }
        for item in views
    ]
    history = {entry["date"]: entry for entry in validate_entries(existing)}
    history.update({entry["date"]: entry for entry in validate_entries(fetched)})
    return [history[day] for day in sorted(history)]


def update_files(root, traffic, refresh_date):
    date.fromisoformat(refresh_date)
    metrics_path = root / "metrics.json"
    existing = json.loads(metrics_path.read_text(encoding="utf-8"))
    merged = merge_metrics(existing, traffic["views"])
    total = sum(entry["count"] for entry in merged)
    badge = f"""<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-{total}-limegreen" alt="Total repository views">
  <p>Refresh Date: {refresh_date}</p>
  <p>GitHub repository views, not website visits.</p>
</div>
<!-- END BADGE -->"""
    updates = {}
    for path in [
        root / "README.md",
        root / "docs" / "overrides" / "partials" / "visitor-counter.html",
    ]:
        content = path.read_text(encoding="utf-8")
        if len(BADGE.findall(content)) != 1:
            raise ValueError(f"Expected exactly one counter badge block in {path}.")
        updates[path] = BADGE.sub(badge, content)
    updates[metrics_path] = json.dumps(merged, indent=2) + "\n"
    for path, content in updates.items():
        path.write_text(content, encoding="utf-8")
    print(f"Updated {len(updates) - 1} badges: {total} repository views.")


if __name__ == "__main__":
    update_files(
        Path.cwd(),
        json.load(sys.stdin),
        datetime.now(timezone.utc).date().isoformat(),
    )
