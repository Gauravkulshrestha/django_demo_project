from csv import list_dialects
from msilib.schema import ListView
from typing import List
from django.contrib import admin
from . models import Employee, Contact

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "age", "gender", "image", "datestamp"]

class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "firstname", "lastname", "email", "desc"]

admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Contact, ContactAdmin)