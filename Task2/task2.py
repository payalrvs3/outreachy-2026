import csv
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

CSV_FILE = "Task 2 - Intern.csv"
MAX_WORKERS = 10

HEADERS = {
    "User-Agent": "Outreachy-URL-Checker/1.0 (payalrvs3; https://github.com/payalrvs3)"
}


def load_urls(csv_file):
    urls = []
    with open(csv_file, newline="") as f:
        reader = csv.DictReader(f) # grab the first column name, whatever it is

        if not reader.fieldnames:
            print("No columns found in CSV")
            return urls

        url_column = reader.fieldnames[0]

        for row in reader:
            url = row[url_column].strip()
            if not url:
                continue
            if not url.startswith(("http://", "https://")):
                url = "http://" + url
            urls.append(url)

    return urls


def get_status(url):
    for _ in range(2):  # retry once on timeout
        try:
            response = requests.head(
                url, headers=HEADERS, timeout=10, allow_redirects=True) # HEAD not allowed, fall back to GET
            if response.status_code == 405:
                response = requests.get(
                    url, headers=HEADERS, timeout=10, allow_redirects=True)
            return url, response.status_code
        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.ConnectionError:
            return url, "CONNECTION_ERROR"
        except requests.exceptions.RequestException as e:
            return url, f"ERROR: {type(e).__name__}"

    return url, "TIMEOUT"


def check_urls(csv_file):
    urls = load_urls(csv_file)
    if not urls:
        return

    results = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(get_status, url): url for url in urls}

        for future in as_completed(futures):
            url, status = future.result()
            results[url] = status
            print(f"({status}) {url}")

    return results


if __name__ == "__main__":
    check_urls(CSV_FILE)
