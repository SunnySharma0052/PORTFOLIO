from django.shortcuts import render, redirect
from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.

def Navbar(request):
    return render(request, 'Navbar.html')

def Project(request):
    return render(request, 'Project.html')

def About(request):
    return render(request, 'About.html')

def Contact_form(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')  # Changed 'E-mail' to 'email' to match the field name
        phone = request.POST.get('phone')
        position = request.POST.get('position')  # Get the position from the POST data

        contact = Contact(First_Name=first_name, Last_Name=last_name, Email=email, Phone=phone)
        if position == 'Front-End':
            contact.position = Contact.FRONT_END
        elif position == 'Back-End':
            contact.position = Contact.BACK_END
        elif position == 'Full_Stack':
            contact.position = Contact.FULL_STACK
        else:
            contact.position = 'Other'

        contact.save()
        messages.success(request, "Your message has been sent!")
        return redirect('Contact')  # Assuming 'contact' is the name of your contact page URL

    return render(request, 'Contact.html', {})