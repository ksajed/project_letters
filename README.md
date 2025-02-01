# project_letters
Letter Generator
Letter Generator is a Django web application that allows you to manage contacts and generate personalized letters based on templates. The application provides complete functionalities for importing, adding, updating, and deleting contacts, as well as managing letter templates. The generated letters are produced as PDF files by extracting content from DOCX templates and replacing dynamic placeholders with contact data.

Main Features
Contact Management:

Add, Update, and Delete Contacts:
Create, update, and delete contacts with information such as name, address, and email.
Import Contacts:
Import multiple contacts from a CSV file using a dedicated import form.
Template Management:

Add and List Templates:
Save letter templates (in DOCX format) containing dynamic placeholders such as {nom}, {adresse}, and {email}.
Template Selection:
When generating a letter, the user can choose the desired template from a global list.
Personalized Letter Generation:

PDF Generation:
The application extracts text from a DOCX template, replaces the placeholders with contact data, and generates a personalized letter in PDF format using ReportLab.
Pagination:

Display contacts with configurable pagination, allowing users to choose the number of contacts displayed per page.
Technologies Used
Django for backend development.
Bootstrap 5 for a modern, responsive design.
ReportLab for dynamic PDF generation.
python-docx for extracting content from DOCX files.
Pandas for importing contacts from CSV files.
Project Structure



letter_generator/
├── manage.py
├── letter_generator/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── letters_app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── utils.py
│   └── ...
├── static/
│   └── css/
│       └── custom.css
└── templates/
    ├── base.html
    ├── index.html
    ├── add_contact.html
    ├── list_contacts.html
    ├── import_contacts.html
    ├── add_template.html
    ├── list_templates.html
    ├── update_contact.html
    ├── confirm_delete.html
    └── choose_template.html




    
Installation
Clone the repository:


git clone https://github.com/your_username/letter_generator.git
cd letter_generator
Create and activate a virtual environment:


python3 -m venv venv
source venv/bin/activate
Install the dependencies:

Ensure you have a requirements.txt file similar to:
Django>=3.2
python-docx
reportlab
pandas

Then run:
pip install -r requirements.txt
Apply the migrations:
python manage.py makemigrations
python manage.py migrate

Run the server:
python manage.py runserver

Usage
Open your web browser and go to http://127.0.0.1:8000/.
Use the navigation menu to:
Manage contacts (add, update, delete, import, list).
Manage letter templates (add, list).
To generate a personalized letter, select a contact and choose a template. The system will generate a PDF with the contact’s details embedded in the template.
Customization

Letter Templates:
Add or modify letter templates via the web interface by uploading DOCX files containing dynamic placeholders (e.g., {nom}, {adresse}, {email}).

Notes
Security:
Ensure that no sensitive information (e.g., secret keys) is exposed in your repository.
Collaboration:
Use Git and GitHub to manage versions and collaborate on the project.
