import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the MIME structure for the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.starttls()  # Upgrade the connection to secure
        server.login(sender_email, sender_password)  # Login to your email account
        server.send_message(message)  # Send the email
        server.quit()  # Close the connection

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage
sender_email = "stockraj@gmail.com"
sender_password = "hrtq qvkt kteo msyb"
recipient_email = "harshraj.2222006@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python!"

send_email(sender_email, sender_password, recipient_email, subject, body)
