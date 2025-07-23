from django.db import models
from PIL import Image
import os

class Category(models.Model):
    name = models.CharField('Заголовок', max_length=100)

    class Meta:
        verbose_name = 'категория'

    def __str__(self):
        return self.name


class GalleryContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField('Заголовок', max_length=200, default='GalleryContent title')
    subtitle = models.TextField('контент', default='GalleryContent subtitle')
    image = models.ImageField('изображение', upload_to='gallery/GalleryContent')

    class Meta:
        verbose_name = 'Галрей контент'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            max_size = (1280, 900)  
            img.thumbnail(max_size, Image.LANCZOS)  
            img_format = img.format
            if img_format == 'JPEG':
                img.save(img_path, format='JPEG', quality=88, optimize=True, progressive=True)
            elif img_format == 'PNG':
                img.save(img_path, format='PNG', optimize=True)
            else:
                img.save(img_path) 
