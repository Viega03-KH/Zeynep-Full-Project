from django.shortcuts import render
from news_app.models import NewsContent
from gallery_app.models import GalleryContent

def home_page(request):
    news_list = NewsContent.objects.order_by('-id')[:5]
    gallery_list = GalleryContent.objects.order_by('-id')
    
    context = {
        'news_list': news_list,
        'gallery_list': gallery_list,
        }
    return render(request, 'pages/home.html', context )




def about_page(request):
    news_list = NewsContent.objects.order_by('-id')[:5]
    gallery_list = GalleryContent.objects.order_by('-id')[:8]
    
    context = {
        'news_list': news_list,
        'gallery_list': gallery_list,
        }
    return render(request, 'pages/about.html', context )



