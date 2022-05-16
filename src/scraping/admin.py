from django.contrib import admin
from .models import City, Language

# Register your models here.

admin.site.register(City)     # регистрация
admin.site.register(Language)