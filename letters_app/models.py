
from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nom

class LetterTemplate(models.Model):
    titre = models.CharField(max_length=255)
    fichier = models.FileField(upload_to="templates/")  # Upload de fichiers .docx
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

