from django.db import models

class Category(models.Model):
    name = models.CharField('Заголовок', max_length=100)
    class Meta:
        verbose_name = 'категория'
    def __str__(self):
        return self.name

class GalleryContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField('Заголовок',max_length=200)
    subtitle = models.TextField('контент')
    image = models.ImageField('изображение', upload_to='gallery/GalleryContent')

    class Meta:
        verbose_name = 'Галрей контент' 
    
    def __str__(self):
        return self.title