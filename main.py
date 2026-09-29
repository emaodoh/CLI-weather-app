from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json
import sys
import os

API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    print("API-KEY not found.")
    sys.exit(1)

def fetch(url):
    try:

        response = urlopen(url)
    
    except HTTPError as e:
        if e.code == 400:
            print("invalid city")
            return

        if e.code == 500:
            print("Server error. Try again later.")
            return 

    except URLError as e:
        print("URL Error", e.reason)
        return

    report = json.load(response)


    format_output(report,save)

def format_output(report,save):
    days = report["days"]
    city = report["address"]
    time_zone = report["timezone"]
    resolved_address = report["resolvedAddress"]

    day = days[0]
    humidity = day["humidity"]
    condition = day["conditions"]
    description = day["description"]
    temp = day["temp"]


    print(f"resolved Address: {resolved_address} ---------------  City: {city} -----------  Time Zone: {time_zone}\nTemperature: {temp} \nHumidity: {humidity} \nCondition: {condition}\nDiscription: {description}")
    if save:
        result = {"resolvedAddress":resolved_address, "city":city, "time_zone": time_zone, "temp":temp, "humidity":humidity, "condition":condition, "description":description}

        file_name = f"{city}_weather.json"

        with open(file_name, "w") as file:
            json.dump(result, file, indent=3)

if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("usage: <file_name> <city> <optional: save>")
        sys.exit(1)

city = sys.argv[1]
save = False

if len(sys.argv) == 3:    
    save  = True

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/tomorrow?key={API_KEY}"


fetch(url)