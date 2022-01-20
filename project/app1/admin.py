from csv import list_dialects
from msilib.schema import ListView
from typing import List
from django.contrib import admin
from . models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "age", "gender", "image", "datestamp"]

admin.site.register(Employee, EmployeeAdmin)