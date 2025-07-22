from django.shortcuts import render
from news_app.models import NewsContent

def home_page(request):
    news_list = NewsContent.objects.order_by('-id')[:5]
    return render(request, 'pages/home.html', {'news_list': news_list})