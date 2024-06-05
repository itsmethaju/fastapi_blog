import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()

# Function to send confirmation email
def send_confirmation_email(email):
    # Set up SMTP connection
    smtp_host = 'smtp.gmail.com'  # Update with your SMTP server
    smtp_port = 587  # Update with your SMTP port
    smtp_username = os.getenv("smtp_username")
    smtp_password = os.getenv("smtp_password")


    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Compose email
    msg = MIMEMultipart()
    msg['From'] = 'tsthaju.me@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Confirmation Email'

    body = 'Thank you for contacting us. Your message has been received.'
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    server.send_message(msg)
    server.quit()