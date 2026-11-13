"""Report on the catalogue-card scanning queue."""

import csv


def pending(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return [row for row in rows if row["status"] != "accepted"]


if __name__ == "__main__":
    for row in pending("queue/card-scans.csv"):
        print(row["card_id"], row["status"])
