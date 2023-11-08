import smtplib
from hidden_items import code_outlook
from hidden_items import code_gmail
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

sender = code_outlook.email       #Use outlook email
receiver = code_gmail.email
PASSWORD = code_outlook.password

# Format rich html email
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

body = """
<h2> Hello there! </h2>
<h3> Just wanted to drop in and say hello!
Hope you are doing well!
</h3>
"""
mimetext = MIMEText(body, 'html')

#Attach file
file_path = 'cute_dog.png'
attachment = open(file_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=file_path)
message.attach(payload=payload)

message.attach(mimetext)
message_text = message.as_string()  #Convert to string
print(message_text)

# Send message
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, PASSWORD)
server.sendmail(sender, receiver, message_text)
print("Email sent!")
server.quit()
