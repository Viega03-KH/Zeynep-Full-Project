from django.contrib import admin
from .models import NewsContent, Category

admin.site.register([ NewsContent, Category ])