import ssl
import smtplib
port = 465 # ssl
smtp_server = "smtp.gmail.com"
sender_email = "abc@gmail.com" #Enter sender Email
receiver_email = "xyz@pqr.com" #Enter receiver Email
password = "purnydoaabflobsu"
message = """Please ignore this, message from pyhton code"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
