from django.urls import path
from .views import add_contact, add_template, choose_template_for_letter, delete_contact, delete_template, import_contacts, generate_letter_view,home, list_contacts, list_templates, send_letter, update_contact, update_template
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('import/', import_contacts, name='import_contacts'),
    path('contacts/', list_contacts, name='list_contacts'),
    path('contacts/add/', add_contact, name='add_contact'),
    path('contacts/update/<int:contact_id>/', update_contact, name='update_contact'),
    path('contacts/delete/<int:contact_id>/', delete_contact, name='delete_contact'),
    #path('generate/<int:contact_id>/<int:template_id>/', generate_letter_view, name='generate_letter'),
    path("generate/<int:contact_id>/", generate_letter_view, name="generate_letter"),  # ✅ Corrigé ici
    path('add-template/', add_template, name='add_template'),
    path('list-templates/', list_templates, name='list_templates'),
    path('choose-template/<int:contact_id>/', choose_template_for_letter, name='choose_template'),
    path('send_letter/<int:contact_id>/', send_letter, name='send_letter'),
    path("templates/update/<int:template_id>/", update_template, name="update_template"),
    path("templates/delete/<int:template_id>/", delete_template, name="delete_template"),
]



    
    

