import smtplib
from email.mime.text import MIMEText
from django.conf import settings

def send_letter_email(to_email, subject, body):
    sender_email = settings.EMAIL_HOST_USER  # Utiliser l'email configuré dans Django
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    
    try:
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(sender_email, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(sender_email, to_email, msg.as_string())
            print(f"Email envoyé à {to_email}")
    except Exception as e:
        print(f"Erreur d'envoi de l'email : {e}")
