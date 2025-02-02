from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, LetterTemplate
import pandas as pd
from django.contrib import messages



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'adresse', 'email']

class ContactImportForm(forms.Form):
    fichier = forms.FileField()

    def clean_fichier(self):
        file = self.cleaned_data.get('fichier')
        if file:
            if not file.name.lower().endswith('.csv'):
                raise forms.ValidationError("Le fichier doit être au format CSV.")
        return file

    def save_contacts(self):
        df = pd.read_csv(self.cleaned_data['fichier'])
        df.columns = [col.strip() for col in df.columns]
    
        for _, row in df.iterrows():
            nom = row['Nom'].strip().lower()  # Normalisation du nom
            email = row['Email'].strip().lower()  # Normalisation de l'email

        # Vous pouvez choisir de vérifier sur le nom, l'email ou les deux.
            if not Contact.objects.filter(email=email).exists():
                Contact.objects.create(
                nom=row['Nom'].strip(),  # ou nom si vous voulez tout en minuscule
                adresse=row['Adresse'].strip(),
                email=email
            )
            else:
                print(f"Le contact avec l'email '{email}' existe déjà et ne sera pas ajouté.")


#gérer l'affichage du formulaire et l'upload des fichiers.              
class LetterTemplateForm(forms.ModelForm):  # Permet d'associer automatiquement les champs du modèle
    class Meta:
        model = LetterTemplate  # Associe ce formulaire au modèle LetterTemplate
        fields = ['titre', 'description', 'fichier']  # Ajoute description aux champs affichés

    # Méthode de validation pour s'assurer que seul un fichier .docx est accepté
    def clean_fichier(self):
        file = self.cleaned_data.get("fichier")  # Récupère le fichier soumis dans le formulaire
        if file:  # Vérifie si un fichier a bien été soumis
            if not file.name.endswith(".docx"):  # Vérifie l'extension du fichier
                raise forms.ValidationError("Seuls les fichiers .docx sont autorisés.")  # Lève une erreur si ce n'est pas un .docx
        return file  # Retourne le fichier validé






    