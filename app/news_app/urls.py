from django.urls import path
from . import views

urlpatterns = [
    path('zeynep-news', views.news_page, name='news_page')
]
