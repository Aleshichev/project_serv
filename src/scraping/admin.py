from django.contrib import admin
from .models import City, Language, Vacancy

# Register your models here.

admin.site.register(City)     # регистрация
admin.site.register(Language)
admin.site.register(Vacancy)