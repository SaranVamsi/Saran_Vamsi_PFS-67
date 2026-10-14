
# Email Automation

import smtplib

from email.message import EmailMessage as em

# EmailMessage - Creates an email message

sender = "saranvamsi.pva@gmail.com"
password = "xajh ffru pdtg ngis"
reciever = "pvasaranvamsi@gmail.com"

msg = em()
msg["Subject"] = "Preparation Email"
msg["From"] = sender
msg["To"] = reciever
msg.set_content("Hello, this is Saran Vamsi from Codegnan.")

# Attach a PDF
file_path = r"C:\Users\saran\Downloads\Coursera K5BDNRAX7RWG.pdf"

with open(file_path, "rb") as file:
    file_data = file.read()

msg.add_attachment(
    file_data,
    maintype="application",
    subtype="pdf",
    filename="Coursera K5BDNRAX7RWG.pdf"
)

# SMTP_SSL - Connects to Gmail's SMTP server using port 465
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("Email sent successfully")
