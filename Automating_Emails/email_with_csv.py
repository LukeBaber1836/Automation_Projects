import yagmail
import os
import pandas

sender = 'lbcoding.1@gmail.com'
PASSWORD = os.environ.get('lbcoding_pw')
df = pandas.read_csv('contacts.csv')

# Opens filename and writes in content
def generate_file(filename, content): 
    with open(filename, 'w') as file:
        file.write(content)

def send_email():
    for index,row in df.iterrows():
        name = row['Name']
        amount = str(row['Amount'])
        attachment = row['Attachment']
        email_addr = row['Email']
        filename = f"{name}_Payment.txt"

        generate_file(filename, amount)
        # Email contents
        subject = f"Hello {name}! This is the subject."
        contents = [f"""
            Hello {name}, you need to pay {amount}.
            The bill is attached below!""", filename]
        
        # Sends email
        yag = yagmail.SMTP(user=sender, password=PASSWORD)
        yag.send(to=email_addr, subject=subject, contents=contents)
        print(f"Email {index+1} sent!")

if __name__ == "__main__":
    send_email()
    