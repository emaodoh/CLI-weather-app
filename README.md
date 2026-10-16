# CLI Weather App

A command-line weather application built with Python that fetches weather information from the Visual Crossing Weather API.

The application allows users to check tomorrow's weather forecast for a city and optionally save the result as a JSON file.

---

## Features

- Fetch weather data from Visual Crossing Weather API
- Search weather by city name
- Display:
  - Temperature
  - Humidity
  - Weather condition
  - Description
  - Time zone
  - Resolved address
- Save weather reports as JSON files
- Secure API key handling using environment variables
- Handles API errors and network failures

---

## Requirements

- Python 3.x
- `requests` package
- Visual Crossing Weather API key

---

## Installation

Clone the repository:

```bash
git clone https://github.com/emaodoh/CLI-weather-app.git

Move into the project directory:
cd cli-weather-app

Install dependencies:
pip install requests

---

API Key Setup

This project uses an environment variable to store the API key.
First, get your API key from Visual Crossing Weather API.
Then export it in your terminal:
Linux / macOS
export WEATHER_API_KEY=<your_api_key>

Example:
export WEATHER_API_KEY=abc123xyz

Windows PowerShell
$env:WEATHER_API_KEY="<your_api_key>"

After setting the key, the application can access it securely without storing it inside the code.

Usage
Run the application:

python3 weather.py <city>

Example:
python weather.py Lagos

Output:
Resolved Address: Lagos, Nigeria

City: Lagos
Time Zone: Africa/Lagos
Temperature: 28.5
Humidity: 70
Condition: Partially cloudy
Description: Partly cloudy throughout the day

Saving Weather Report
To save the weather result as a JSON file:
python weather.py <city> save

Example:
python weather.py London save

This will create a file:
London_weather.json

Example JSON output:
{
   "resolvedAddress": "London, UK",
   "city": "London",
   "time_zone": "Europe/London",
   "temp": 15.4,
   "humidity": 80,
   "condition": "Partially cloudy",
   "description": "Partly cloudy throughout the day"
}

Error Handling
The application handles common errors:
Missing API Key
If the API key is not exported:
API-KEY not found.

Invalid API Key
Invalid API key

Invalid City
Invalid city

Network Problems
Network error. Check your internet connection.

Request Timeout
Request timed out. Try again.

Project Structure
cli-weather-app/
│
├── weather.py
├── README.md

How It Works
1. User enters a city name through the command line.
2. The application reads the API key from the environment variable.
3. A GET request is sent to the Visual Crossing Weather API.
4. The JSON response is processed.
5. Weather information is displayed.
6. The user can optionally save the report as a JSON file.

Technologies Used
- Python
- Requests Library
- JSON
- Visual Crossing Weather API
- Environment Variables

Future Improvements
Possible improvements:
- Add weather forecast for multiple days
- Add command-line argument parsing using argparse
- Add unit tests
- Add colored terminal output
- Add caching to reduce API calls
- Add automatic retry handling for API rate limits

Author

Emmanuel
