import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SENDER_EMAIL = os.getenv("CB_EMAIL")
APP_PASSWORD = os.getenv("CB_EMAIL_PWD")

def send_email(receiver_emails: list, subject: str, body: str):
    if not SENDER_EMAIL or not APP_PASSWORD:
        raise EnvironmentError("Missing SENDER_EMAIL or GOOGLE_APP_PASSWORD in .env file")

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(receiver_emails)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_emails, msg.as_string())
            print(f"\n✅ Email sent successfully to: {', '.join(receiver_emails)}")
    except Exception as e:
        print(f"\n❌ Failed to send email: {e}")

if __name__ == "__main__":
    print("📧 Multi-Recipient Email Sender\n")

    receivers_input = input("Enter receiver emails (comma-separated): ").strip()
    receiver_emails = [email.strip() for email in receivers_input.split(",") if email.strip()]

    subject = input("Enter subject: ").strip()
    print("Enter message body (type 'END' on a new line to finish):")
    body_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        body_lines.append(line)
    body = "\n".join(body_lines)

    send_email(receiver_emails, subject, body)
