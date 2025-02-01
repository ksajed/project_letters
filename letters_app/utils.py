import os
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def extract_text_from_docx(docx_path):
    """
    Extrait le texte du fichier DOCX en concaténant tous les paragraphes.
    """
    with open(docx_path, "rb") as f:
        doc = Document(f)
    paragraphs = [para.text for para in doc.paragraphs]
    return "\n".join(paragraphs)

def generate_letter_pdf(contact, template_path):
    """
    Génère un PDF personnalisé pour un contact donné.
    Le contenu est extrait depuis un template DOCX situé à template_path.
    Les balises {nom}, {adresse} et {email} sont remplacées par les informations du contact.
    Le PDF est mis en page de façon améliorée pour une lecture plus agréable.
    """
    # Extraire le texte du template DOCX
    template_text = extract_text_from_docx(template_path)
    
    # Remplacer les balises par les valeurs du contact
    letter_text = template_text.replace("{nom}", contact.nom)
    letter_text = letter_text.replace("{adresse}", contact.adresse)
    letter_text = letter_text.replace("{email}", contact.email)
    
    # Définir le chemin de sortie pour le PDF
    output_dir = "generated_letters"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = f"{contact.nom}.pdf"
    output_path = os.path.join(output_dir, output_filename)
    
    # Créer le document PDF avec ReportLab
    doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)
    
    # Définir les styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "title", 
        parent=styles["Heading1"], 
        alignment=1,  # Centré
        spaceAfter=20
    )
    normal_style = ParagraphStyle(
        "normal",
        parent=styles["Normal"],
        fontSize=12,
        leading=15,
        spaceAfter=12
    )
    
    # Construction des éléments du PDF
    elements = []
    
    # Titre de la lettre
    elements.append(Paragraph("Lettre Personnalisée", title_style))
    
    # Vous pouvez ajouter ici une date ou un objet si souhaité
    # Par exemple :
    # elements.append(Paragraph("Date : {date}", normal_style))
    # elements.append(Paragraph("Objet : Demande d'information", normal_style))
    
    # Séparer le texte en lignes (ou paragraphes) à partir des retours à la ligne
    paragraphs = letter_text.split("\n")
    for para in paragraphs:
        para = para.strip()
        if para:
            elements.append(Paragraph(para, normal_style))
    
    # Générer le PDF
    doc.build(elements)
    
    return output_path
