import smtplib, ssl
import json

with open('../osvar/email.txt') as f:
    a = f.read()
email = json.loads(a)

smtp_server = 'smtp.qiye.163.com'
port = 465
sender_email = email['name']
receiver_email = 'linzhiyu0@gmail.com'
password= email['code']

# Create a secure SSL context
context = ssl.create_default_context()

message = """\
Subject: Hi there

This message is a test"""

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 