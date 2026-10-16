import requests
import json
import sys
import os


API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    print(
        "API-KEY not found.\n"
        "Usage:\n"
        "export WEATHER_API_KEY=<your_api_key>"
    )
    sys.exit(1)


def fetch(url, save):

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 401:
            print("Invalid API key")
            return

        if response.status_code == 400:
            print("Invalid city")
            return

        response.raise_for_status()

        report = response.json()

        format_output(report, save)

    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")

    except requests.exceptions.ConnectionError:
        print("Network error. Check your internet connection.")

    except requests.exceptions.RequestException:
        print("Something went wrong with the request.")


def format_output(report, save):

    days = report["days"]
    city = report["address"]
    time_zone = report["timezone"]
    resolved_address = report["resolvedAddress"]

    day = days[0]

    humidity = day["humidity"]
    condition = day["conditions"]
    description = day["description"]
    temp = day["temp"]

    print(
        f"Resolved Address: {resolved_address}\n"
        f"City: {city}\n"
        f"Time Zone: {time_zone}\n"
        f"Temperature: {temp}\n"
        f"Humidity: {humidity}\n"
        f"Condition: {condition}\n"
        f"Description: {description}"
    )

    if save:
        result = {
            "resolvedAddress": resolved_address,
            "city": city,
            "time_zone": time_zone,
            "temp": temp,
            "humidity": humidity,
            "condition": condition,
            "description": description
        }

        file_name = f"{city}_weather.json"

        with open(file_name, "w") as file:
            json.dump(result, file, indent=3)


if len(sys.argv) not in [2, 3]:
    print("usage: python weather.py <city> <optional: save>")
    sys.exit(1)


city = sys.argv[1]

save = len(sys.argv) == 3


url = (
    f"https://weather.visualcrossing.com/"
    f"VisualCrossingWebServices/rest/services/timeline/"
    f"{city}/tomorrow?key={API_KEY}"
)


fetch(url, save)