import smtplib
import emails_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config_server = "smtp.gmail.com"
config_server_port = 587
config_email = "sendermail@gmail.com"
config_password = "password"

def envoyer_email(email_destinataire, sujet, message):
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = emails_config.config_email
    multipart_message['To'] = email_destinataire
    multipart_message.attach(MIMEText(message,"plain")) # type: ignore
    
    serveur_mail = smtplib.SMTP(emails_config.config_server,emails_config.config_server_port)
    serveur_mail.starttls()
    serveur_mail.login(emails_config.config_email,emails_config.config_password)
    serveur_mail.sendmail(emails_config.config_email,email_destinataire,
    multipart_message.as_string())
    serveur_mail.quit()
    
message_email = """ Bonsoir,

Ceci est un test de mail automatique par un script Python.

Cordialement,

Fehizoro Andry RAKOTOARINOSY.
"""
    
envoyer_email("receiver@gmail.com","Test send Email by script Python",message_email)