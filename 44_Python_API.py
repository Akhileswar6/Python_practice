# Making API Requests in Python
# In order to work with APIs, some tools are required, such as requests module and we need to first install them in our system.

# cmd -> pip install requests


# Example 1: Fetching Live Stock Price
import requests

def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else:
        return None

price = get_stock_data()
symbol = "IBM"
if price is not None:
    print(f"{symbol}: {price}")
else:
    print("Failed to retrieve data.")



# Understanding API Status Codes

# 200 OK: Request successful, data returned.
# 201 Created: New resource created.
# 204 No Content: Success but no data returned.
# 400 Bad Request: Invalid request.
# 401 Unauthorized: Missing or invalid API key.
# 500 Internal Server Error: Server encountered an error.


print("\n" + "="*50 + "\n")

# Example 2: Fetching News Headlines Using NewsAPI

import json
import requests

def jprint(obj):
    """Pretty-print JSON objects with indentation."""
    print(json.dumps(obj, sort_keys=True, indent=4))

def fetch_and_print_articles(api_url):
    """Fetch and print articles from the News API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        data = response.json()
        articles = data.get('articles', [])
        
        if not articles:
            print("No articles found.")
            return
        
        for index, article in enumerate(articles[:1], start=1):
            print(f"Article {index}:")
            jprint(article)
            print()

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Use your actual API key here
API_KEY = '60703cb000b44493a0db2485ced97b2e'

api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

fetch_and_print_articles(api_endpoint)


print("\n" + "="*50 + "\n")

# Using Query Parameters in API Requests
import requests

API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "60703cb000b44493a0db2485ced97b2e"

params = {
    "country": "us",
    "apiKey": API_KEY,
    "pageSize": 1
}

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")



print("\n" + "="*50 + "\n")



# Example 3: Tracking the International Space Station (ISS) Location
# json: For decoding JSON data from API.
# turtle: For graphical map display.
# urllib.request: To fetch API data.
# time: For periodic updates.
# webbrowser: To open files.
# geocoder: To find current user location.


import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# Fetch current astronauts data from the API
astronauts_url = "http://api.open-notify.org/astros.json"
with urllib.request.urlopen(astronauts_url) as response:
    astronauts_data = json.loads(response.read())

# Write astronauts info to a text file
with open("iss.txt", "w") as file:
    file.write(f"There are currently {astronauts_data['number']} astronauts on the ISS:\n\n")
    for person in astronauts_data["people"]:
        file.write(f"{person['name']} - onboard\n")

    # Get user's current latitude and longitude
    user_location = geocoder.ip('me')
    file.write(f"\nYour current lat / long is: {user_location.latlng}")

# Open the text file in the default web browser
webbrowser.open("iss.txt")

# Setup the turtle screen for ISS tracking map
screen = turtle.Screen()
screen.setup(width=1280, height=720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load world map and ISS icon
screen.bgpic("images/map.gif")
screen.register_shape("images/iss.gif")

# Create the turtle representing the ISS
iss = turtle.Turtle()
iss.shape("images/iss.gif")
iss.setheading(45)
iss.penup()

# API endpoint to get ISS current position
iss_position_url = "http://api.open-notify.org/iss-now.json"

try:
    while True:
        with urllib.request.urlopen(iss_position_url) as response:
            data = json.loads(response.read())

        lat = float(data["iss_position"]["latitude"])
        lon = float(data["iss_position"]["longitude"])

        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")

        # Update ISS position on map
        iss.goto(lon, lat)

        # Pause for 5 seconds before updating again
        time.sleep(5)

except KeyboardInterrupt:
    print("\nISS tracking stopped by user.")
    turtle.bye()  # Close turtle window cleanly
