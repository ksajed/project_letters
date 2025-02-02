from django.core.mail import send_mail
from django.conf import settings

def envoyer_email():
    sender_email = settings.EMAIL_HOST_USER  # Récupérer l'email configuré
    subject = "Bienvenue !"
    message = "Merci de vous être inscrit sur notre site."
    recipient_list = ["utilisateur@example.com"]

    send_mail(
        subject,
        message,
        sender_email,  # Expéditeur
        recipient_list,
        fail_silently=False,
    )
