#form
from django.shortcuts import redirect, render
from .forms import RegistrationForm

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:       
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})
