import requests
import json

URL = "https://media730-fast-track-prd-emea-68dacb8178d61.clyche.pro/h98H1H48izQD1UvJUjjpgOdWjuJvJ5AC/data76.json"
OUTPUT_FILE = "events.json"

def main():
    # Fetch the full JSON
    r = requests.get(URL, headers={"User-Agent": "python-requests/2.31.0"})
    r.raise_for_status()
    data = r.json()

    # Extract only events
    events = data.get("data", {}).get("events", [])

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(events)} event categories to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
