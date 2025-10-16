"""
app/utils/csv_utils.py
Simple CSV export and formatting utility.
"""

import csv
from datetime import datetime


def export_to_csv(data: list, filename: str, headers: list):
    """
    Exports given data (list of dicts) to CSV file.
    """

    csv_name = f"{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(csv_name, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"[CSV Export] Saved {csv_name}")
    return csv_name


def format_value(value):
    """
    Format value before writing to CSV.
    - Float -> two decimals
    - Bool -> Yes/No
    - None -> empty
    """
    if value is None:
        return ""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)