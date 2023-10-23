import yagmail
import os
import time

sender = 'lbcoding.1@gmail.com'
PASSWORD = os.environ.get('lbcoding_pw')

receiver = 'gxnsahsqe@emlpro.com'   #Temp email from: https://dropmail.me/en/
num = 0
while True:
    subject = f"This is email {num}"
    contents = f"""
        Here is a random email that I am sending with Python!
        Hi from {num}!
    """
    yag = yagmail.SMTP(user=sender, password=PASSWORD)
    yag.send(to=receiver, subject=subject, contents=contents)
    num +=1
    print("Email sent!")
    time.sleep(60)