from django.shortcuts import render
from .models import NewsContent


def news_page(request):
    news_list = NewsContent.objects.order_by('-id')[:10]
    
    context = {
        'news_list': news_list,
        }
    return render(request, 'pages/news.html', context )