import datetime
from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":

        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        desc = request.POST.get("desc")

        contacts = Contact(firstname=firstname,lastname=lastname,email=email,desc=desc)
        contacts.save()

    return render(request, "contact.html")