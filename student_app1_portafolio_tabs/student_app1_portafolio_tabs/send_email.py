import smtplib


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = ""
    password = ""

    with smtplib.SMTP_SSL(host, port) as sender:
        sender.login(username, password)
        sender.sendmail(username, username, message)
