import os
import smtplib

import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("PY_EMAIL")
    password = os.getenv("PY_PASSWORD")

    with smtplib.SMTP_SSL(host, port) as sender:
        sender.login(username, password)
        sender.sendmail(from_addr=username, to_addrs=username, msg=message)
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
            send_email(message="Hey, new event was found!")
