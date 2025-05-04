from django.urls import path
from djangoproject.phonebook.views import landing_page, create_contact, delete_contact

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('new-contact', create_contact, name='new-contact'),
    path('delete/<int:contact_id>', delete_contact, name='delete')
]