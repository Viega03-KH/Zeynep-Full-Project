from django.db import models

class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='home/HomeContent')

    def __str__(self):
        return self.title
    

class TestimonialsContent(models.Model):
    full_name = models.CharField(max_length=200)
    commint = models.TextField()
    author = models.ImageField(upload_to='home/TestimonialsContent')

    def __str__(self):
        return self.full_name