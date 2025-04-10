#Write a python Program to send email to any email address.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(sender_email, sender_password, receiver_email, subject, message):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)
sender_email = "nausheentasneem07@gmail.com"
sender_password = "tasneem@7"
receiver_email = "tasneem.shaikh0703@gmail.com"
subject = "Test Email"
message = "This is a test email sent from Python."
send_email(sender_email, sender_password, receiver_email, subject, message)
