from django.core.mail import send_mail
from django.conf import settings
import logging

send_mail(
    "Test Email",
    "Ceci est un test d'email.",
    settings.EMAIL_HOST_USER,
    ["khalidsajed1975@gmail.comt@gmail.com"],
    fail_silently=False,
)



logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
