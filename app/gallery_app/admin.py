from django.contrib import admin
from .models import Category, GalleryContent

@admin.register(GalleryContent)
class GalleryContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'image')
    search_fields = ('title', 'subtitle')
    list_filter = ('category',)
    list_per_page = 20

    fieldsets = (
        ('TITLE', {
            'classes': ('collapse',),
            'fields': ('title_uz', 'title_ru', 'title_en', 'title_tr')
        }),
        ('SUBTITLE', {
            'classes': ('collapse',),
            'fields': ('subtitle_uz', 'subtitle_ru', 'subtitle_en', 'subtitle_tr')
        }),
        ('IMAGE', {
            'classes': ('collapse',),
            'fields': ('category','image',)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')             
    search_fields = ('name',)                
    list_per_page = 20       