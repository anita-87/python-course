import requests
from datetime import datetime
from selectorlib import Extractor

URL = "https://programmer100.pythonanywhere.com/"


def get_temperature():
    response = requests.get(URL)
    extractor = Extractor.from_yaml_file("extract.yml")
    return extractor.extract(response.text)["temperature"]


def get_date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d-%H-%M-%S")


def store_data(date, temp):
    header = True
    with open("data.csv", "r") as file:
        header_line = file.readline()
        if header_line == "":
            header = False
    with open("data.csv", "a") as file:
        if not header:
            file.write("date,temperature\n")
        file.write(f"{date},{temp}\n")


if __name__ == "__main__":
    temperature = get_temperature()
    current_date = get_date()
    store_data(current_date, temperature)
