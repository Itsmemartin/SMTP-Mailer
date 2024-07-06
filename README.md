# SMTP-Mailer
SMTP Mailer is a simple Python script for sending emails via SMTP.
This project shows how to connect to an SMTP server, authenticate using an app password, and send an email(s) with a subject and body to one or multiple emails as per your needs.

Features:
- Connects to SMTP servers (e.g., Gmail)
- Authenticates with an app password
- Sends plain text emails by default (can be upgraded to emails with HTML/Attachments/Inline Images)
  
Requirements:
- Python 3.x
- smtplib (standard library)
- email (standard library)
  
Usage:
- Generate an app password for your email account (e.g., [Gmail](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiHh7af5JGHAxXNnK8BHe6fGCEQFnoECBQQAQ&url=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&usg=AOvVaw1rVibBR6kQTiUjqa0l_f8W&opi=89978449)).
- Update the script with your email, app password, and recipient email(s).
- Run the script to send the email(s).
