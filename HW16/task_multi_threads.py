import requests
import time
import threading

# https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&hourly=temperature_2m LONDON
# https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m NEW YORK
# https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&hourly=temperature_2m TOKYO
# https://api.open-meteo.com/v1/forecast?latitude=34.05&longitude=-118.24&hourly=temperature_2m LOS ANGELES
# https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&hourly=temperature_2m PARIS

# result = dict()
#
#
# def calculate_average(temperatures, town):
#     temperatures_sum = 0
#     count = 0
#     for item in temperatures:
#         temperatures_sum += item
#         count += 1
#     average_value = round(temperatures_sum / count, 2)
#     result[town] = average_value
#
#


def get_key(d, temp):
    for key, value in d.items():
        if temp == value:
            return key


req = [
    {"name": "London", "latitude": 51.51, "longitude": -0.13},
    {"name": "New York", "latitude": 40.71, "longitude": -74.01},
    {"name": "Tokyo", "latitude": 35.69, "longitude": 139.69},
    {"name": "Los Angeles", "latitude": 34.05, "longitude": -118.24},
    {"name": "Paris", "latitude": 48.85, "longitude": 2.35}
]

result = dict()


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
    new_element = {town["name"]: average_value}
    result.update(new_element)


def multi_thread():
    threads = list()

    for item in req:
        threads.append(threading.Thread(target=get_average_temperature, args=(item, )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(result)
    max_temperature = max(result.values())
    town = get_key(result, max_temperature)
    print(f"The hottest temperature: {max_temperature} in {town}")


if __name__ == '__main__':
    start = time.time()
    multi_thread()
    print(f"Program ended in {time.time() - start}")
