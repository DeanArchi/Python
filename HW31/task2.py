import requests

user_input = input("Input your city: ")

res = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={user_input}")
try:
    data = res.json()["results"][0]

    town_coordinates = {
        "latitude": data["latitude"],
        "longitude": data["longitude"]
    }

    request = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": town_coordinates["latitude"],
            "longitude": town_coordinates["longitude"],
            "current_weather": True
        }
    )
    current_weather = request.json()
    temperature = current_weather["current_weather"]["temperature"]
    print(f"In {user_input} the temperature now is {temperature}")
except KeyError:
    print("No results found.")




