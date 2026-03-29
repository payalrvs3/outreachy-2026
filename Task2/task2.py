import csv
import requests

CSV_FILE = "Task 2 - Intern.csv"

HEADERS = {
    "User-Agent": "Outreachy-URL-Checker/1.0 (payalrvs3; https://github.com/payalrvs3)"
}


def check_urls(csv_file):
    with open(csv_file, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)  # grab the first column name, whatever it is

        if not reader.fieldnames:
            print("No columns found in CSV")
            return

        url_column = reader.fieldnames[0]

        with open("output.csv", "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerow(["URL", "Status"])

            for row in reader:
                url = row[url_column].strip()

                if not url: # skip empty rows
                    continue

                if not url.startswith(("http://", "https://")):
                    url = "http://" + url

                status = get_status(url)
                print(f"({status}) {url}")
                writer.writerow([url, status])


def get_status(url):
    for _ in range(2):  # retry once on timeout
        try:
            response = requests.head(
                url, headers=HEADERS, timeout=10, allow_redirects=True) # HEAD not allowed, fall back to GET

            if response.status_code == 405:
                response = requests.get(
                    url, headers=HEADERS, timeout=10, allow_redirects=True)

            return response.status_code

        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.ConnectionError:
            return "CONNECTION_ERROR"
        except requests.exceptions.RequestException as e:
            return f"ERROR: {str(e)}"

    return "TIMEOUT"


if __name__ == "__main__":
    check_urls(CSV_FILE)
