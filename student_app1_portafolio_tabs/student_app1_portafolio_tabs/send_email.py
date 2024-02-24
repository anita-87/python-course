import os
import smtplib


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("PY_EMAIL")
    password = os.getenv("PY_PASSWORD")

    with smtplib.SMTP_SSL(host, port) as sender:
        sender.login(username, password)
        sender.sendmail(username, username, message)
