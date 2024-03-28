import requests

API_KEY = ""


def get_data(place, forecast_days):
    nr_values = 8 * forecast_days
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&cnt={nr_values}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokio", 3))
