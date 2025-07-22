from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'категория'
    def __str__(self):
        return self.name


class NewsContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = RichTextUploadingField()
    image = models.ImageField(upload_to='home/HomeContent')
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)     

    class Meta:
        verbose_name = 'Новости контент'

    def __str__(self):
        return self.title

