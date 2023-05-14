import requests
import time
import multiprocessing

# https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&hourly=temperature_2m LONDON
# https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m NEW YORK
# https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&hourly=temperature_2m TOKYO
# https://api.open-meteo.com/v1/forecast?latitude=34.05&longitude=-118.24&hourly=temperature_2m LOS ANGELES
# https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&hourly=temperature_2m PARIS

req = [
    {"name": "London", "latitude": 51.51, "longitude": -0.13},
    {"name": "New York", "latitude": 40.71, "longitude": -74.01},
    {"name": "Tokyo", "latitude": 35.69, "longitude": 139.69},
    {"name": "Los Angeles", "latitude": 34.05, "longitude": -118.24},
    {"name": "Paris", "latitude": 48.85, "longitude": 2.35}
]


def get_key(d, temp):
    for key, value in d.items():
        if temp == value:
            return key


def get_average_temperature(town):
    request = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": town["latitude"],
            "longitude": town["longitude"],
            "hourly": "temperature_2m"
        }
    )
    temperature_list = request.json()["hourly"]["temperature_2m"]
    average_value = round(sum(temperature_list) / len(temperature_list), 2)
    return town["name"], average_value


def multi_process():
    with multiprocessing.Pool(5) as pool:
        result = dict(pool.map(get_average_temperature, req))
    print(result)
    max_temperature = max(result.values())
    town = get_key(result, max_temperature)
    print(f"The hottest temperature: {max_temperature} in {town}")


if __name__ == '__main__':
    start = time.time()
    multi_process()
    print(f"Program ended in {time.time() - start}")
