from django.shortcuts import render
from .models import GalleryContent


def gallery_page(request):
    gallery_list = GalleryContent.objects.order_by('-id')[:10]
    
    context = {
        'gallery_list': gallery_list,
        }
    return render(request, 'pages/gallery.html', context )