import yagmail
import os
import time
from datetime import datetime as dt

sender = 'lbcoding.1@gmail.com'
PASSWORD = os.environ.get('lbcoding_pw') #Enviroment variable stores pw

receiver = 'gxnsahsqe@emlpro.com'   #Temp email from: https://dropmail.me/en/
num = 0
while True:
    now = dt.now()
    # Sends an email at 5:29 CDT
    if now.hour == 17 and now.minute == 29:
        subject = f"This is you daily email {num}"
        contents = f"""
            Here is a random email that I am sending with Python!
            Hi from {num}!
        """
        yag = yagmail.SMTP(user=sender, password=PASSWORD)
        yag.send(to=receiver, subject=subject, contents=contents)
        num +=1
        print("Email sent!")
        time.sleep(60)