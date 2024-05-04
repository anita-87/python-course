import os
import smtplib
import imghdr
from email.message import EmailMessage


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    username = os.getenv("PY_EMAIL")
    password = os.getenv("PY_PASSWORD")

    gmail = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(from_addr=username, to_addrs=username, msg=email_message.as_string())
    gmail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")
