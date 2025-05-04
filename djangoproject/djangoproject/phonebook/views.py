from django.shortcuts import render, redirect, get_object_or_404

from djangoproject.phonebook.models import Contact


def landing_page(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook/index.html', {'contacts': contacts})

def create_contact(request):
    name = request.POST['name']
    number = request.POST['number']
    contact = Contact(
        name=name,
        number=number
    )
    contact.save()
    return redirect('landing_page')

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('landing_page')