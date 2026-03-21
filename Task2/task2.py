import csv
import requests

CSV_FILE = "Task 2 - Intern.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

with open(CSV_FILE, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    # grab the first column name, whatever it is
    url_column = reader.fieldnames[0]
    for row in reader:
        url = row[url_column].strip()
        if not url:  # skip empty rows
            continue
        try:
            response = requests.head(
                url, headers=HEADERS, timeout=10, allow_redirects=True)
            if response.status_code == 405:  # HEAD not allowed, fall back to GET
                response = requests.get(
                    url, headers=HEADERS, timeout=10, allow_redirects=True)
            status = response.status_code
        except requests.exceptions.RequestException:
            status = "ERROR"
        print(f"({status}) {url}")
