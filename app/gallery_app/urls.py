from django.urls import path
from . import views

urlpatterns = [
    path('zeynep-gallery', views.gallery_page, name='gallery_page'),
]
