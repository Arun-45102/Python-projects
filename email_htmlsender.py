import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('html/index.html').read_text())
email = EmailMessage()
email['from'] = "Arun Kumar M"
email['to'] = "arun2451.a2@gmail.com"
email['subject'] = "This is test python mail"
email.set_content(html.substitute({'name': 'Arun'}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("arun1356189@gmail.com", "@Run45102")
    smtp.send_message(email)
    print("mail done")
