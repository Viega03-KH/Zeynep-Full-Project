from django.contrib import admin
from .models import HomeContent

admin.site.register(HomeContent)



admin.site.site_header = "Zeynap"
admin.site.site_title = "Zeynap Admin"
admin.site.index_title = "Boshqaruv paneliga xush kelibsiz"