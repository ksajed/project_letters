from django.shortcuts import redirect, render, get_object_or_404
from django.http import FileResponse
from .models import Contact, LetterTemplate
from .forms import ContactForm, ContactImportForm, LetterTemplateForm
from django.shortcuts import render
from django.contrib import messages  # Optionnel : pour afficher des messages à l'utilisateur
from .forms import ContactImportForm
from django.core.paginator import Paginator

def home(request):
    return render(request, "index.html")
def import_contacts(request):
    if request.method == "POST":
        form = ContactImportForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save_contacts()
                messages.success(request, "Les contacts ont été importés avec succès !")
            except Exception as e:
                messages.error(request, f"Une erreur est survenue lors de l'importation des contacts : {str(e)}")
        else:
            # Les erreurs de validation du formulaire (par exemple, le fichier n'est pas CSV)
            messages.error(request, "Erreur dans le formulaire : " + str(form.errors.get('fichier', [''])[0]))
    else:
        form = ContactImportForm()

    return render(request, "import_contacts.html", {"form": form})


def generate_letter_view(request, contact_id, template_id):
    from django.shortcuts import get_object_or_404
    from django.http import FileResponse
    from .models import Contact, LetterTemplate
    from .utils import generate_letter_pdf  # Import de la fonction mise à jour

    contact = get_object_or_404(Contact, id=contact_id)
    template = get_object_or_404(LetterTemplate, id=template_id)
    
    output_path = generate_letter_pdf(contact, template.fichier.path)
    
    return FileResponse(open(output_path, "rb"), as_attachment=True, filename=f"{contact.nom}.pdf")

def list_contacts(request):
    # Récupérer tous les contacts ordonnés par nom
    contacts_list = Contact.objects.all().order_by('nom')
    
    # Récupérer le paramètre 'items' depuis l'URL, par défaut à 5 si non précisé
    try:
        items_per_page = int(request.GET.get('items', 5))
        if items_per_page <= 0:
            items_per_page = 5
    except ValueError:
        items_per_page = 5

    # Créer le paginator avec le nombre d'items par page
    paginator = Paginator(contacts_list, items_per_page)
    
    # Récupérer le numéro de page (si présent)
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    
    context = {
        "contacts": contacts,
        "items_per_page": items_per_page,
    }
    return render(request, "list_contacts.html", context)



def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    # Si le formulaire de confirmation est soumis (méthode POST)
    if request.method == "POST":
        contact.delete()
        messages.success(request, f"Le contact '{contact.nom}' a été supprimé avec succès.")
        return redirect('list_contacts')
    
    # Afficher la page de confirmation pour la suppression (méthode GET)
    return render(request, "confirm_delete.html", {"contact": contact})


def update_contact(request, contact_id):
    """Modifie un contact existant."""
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Le contact a été mis à jour avec succès.")
            return redirect('list_contacts')
        else:
            messages.error(request, "Erreur lors de la mise à jour du contact.")
    else:
        form = ContactForm(instance=contact)
    return render(request, "update_contact.html", {"form": form, "contact": contact})


def add_contact(request):
    """Ajoute un nouveau contact."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le contact a été ajouté avec succès.")
            return redirect('list_contacts')
        else:
            messages.error(request, "Erreur lors de l'ajout du contact. Veuillez vérifier les informations fournies.")
    else:
        form = ContactForm()
    return render(request, "add_contact.html", {"form": form})



def add_template(request):
    """
    Vue permettant d'ajouter un nouveau template de lettre.
    """
    if request.method == "POST":
        form = LetterTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Le modèle de lettre a été ajouté avec succès !")
            # Rediriger vers la liste des templates ou vers la page d'accueil
            return redirect('list_templates')  # Vous pouvez définir une vue 'list_templates'
            # ou return redirect('home')
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les informations fournies.")
    else:
        form = LetterTemplateForm()

    return render(request, "add_template.html", {"form": form})

def list_templates(request):
    templates = LetterTemplate.objects.all()
    return render(request, "list_templates.html", {"templates": templates})

def choose_template_for_letter(request, contact_id):
    """
    Vue qui permet de choisir le template de lettre à utiliser pour générer la lettre pour un contact donné.
    """
    # Récupération du contact pour lequel la lettre sera générée
    contact = get_object_or_404(Contact, id=contact_id)
    # Récupération de tous les templates disponibles (liste globale)
    templates = LetterTemplate.objects.all()

    if request.method == "POST":
        # Récupérer l'ID du template sélectionné depuis le formulaire
        selected_template_id = request.POST.get('template_id')
        if selected_template_id:
            # Rediriger vers la vue qui génère la lettre, en passant l'ID du contact et du template
            return redirect('generate_letter', contact_id=contact.id, template_id=selected_template_id)
        else:
            messages.error(request, "Veuillez sélectionner un template.")

    return render(request, "choose_template.html", {"contact": contact, "templates": templates})

