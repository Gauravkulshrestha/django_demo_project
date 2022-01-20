from unicodedata import name
from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    allemp = Employee.objects.all()

    return render(request, "index.html", {"allemp":allemp})