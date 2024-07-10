import smtplib
from email.mime.text import MIMEText

# Define your email server details and login credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'gmail@example.com'
EMAIL_PASSWORD = 'your_gmail_password'
def send_email_alert(recipient, subject, message):
    sender = "your_email@example.com"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP("smtp.example.com") as server:
        server.login("username", "password")
        server.sendmail(sender, [recipient], msg.as_string())

# Example usage
send_email_alert('recipient@example.com', 'Traffic Alert', 'High traffic detected')
