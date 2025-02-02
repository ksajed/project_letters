
from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom du Contact")
    adresse = models.TextField(verbose_name="Adresse")  # ✅ Ajout d'une adresse
    email = models.EmailField(verbose_name="Email")  # ✅ Ajout de l'email

    def __str__(self):
        return self.nom

from django.db import models

class LetterTemplate(models.Model):
    titre = models.CharField(max_length=255)  # Titre du template
    description = models.TextField(blank=True, null=True)  # Champ de description facultatif
    fichier = models.FileField(upload_to="templates/")  # Upload de fichiers .docx
    date_ajout = models.DateTimeField(auto_now_add=True)  # Date d'ajout automatique

    def __str__(self):
        return self.titre


