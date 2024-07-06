import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    #your email here
    from_email = "senders_email"

    #your app password here
    password = "##########"
  
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try: 
        #      your SMTP server address provided by your mailing service
        server = smtplib.SMTP('*SERVER_ADDRESS_HERE*', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

#List of email(s) you want to send your message to
email_list = ["","","","",""]

#The Subject of your Email
Email_subject = ""

#The Body of your Email
Email_body = ""
for i in range(len(email_list)):
    send_email(Email_subject, Email_body, f"{email_list[i]}")
