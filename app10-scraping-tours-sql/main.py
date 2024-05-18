import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def send_email():
    print("Email was sent!")


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted_text):
    with open("data.txt", "a") as file:
        file.write(extracted_text + "\n")


def read():
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scrapped = scrape(URL)
    extracted = extract(scrapped)
    print(extracted)
    content = read()
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email()
