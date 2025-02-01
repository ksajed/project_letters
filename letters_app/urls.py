from django.urls import path
from .views import add_contact, add_template, choose_template_for_letter, delete_contact, import_contacts, generate_letter_view,home, list_contacts, list_templates, update_contact

urlpatterns = [
    path('', home, name='home'),
    path('import/', import_contacts, name='import_contacts'),
    path('contacts/', list_contacts, name='list_contacts'),
    path('contacts/add/', add_contact, name='add_contact'),
    path('contacts/update/<int:contact_id>/', update_contact, name='update_contact'),
    path('contacts/delete/<int:contact_id>/', delete_contact, name='delete_contact'),
    path('generate/<int:contact_id>/<int:template_id>/', generate_letter_view, name='generate_letter'),
    path('add-template/', add_template, name='add_template'),
    path('list-templates/', list_templates, name='list_templates'),
    path('choose-template/<int:contact_id>/', choose_template_for_letter, name='choose_template'),
]
