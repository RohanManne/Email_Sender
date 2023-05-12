from email.message import EmailMessage
from app2 import password
import ssl, smtplib


email_sender = 'SampleEmail'
email_password = password

email_reciever = 'SampleEmail'
subject =  "Greetings"
body = """
Have a good day
"""

em = EmailMessage()

em['From'] = email_reciever
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())