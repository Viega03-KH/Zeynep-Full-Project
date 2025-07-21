from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class NewsContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='home/HomeContent')
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)      

    def __str__(self):
        return self.title

