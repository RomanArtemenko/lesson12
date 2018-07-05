from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Article


# Create your views here.
# def index(request):
#     return render(request, 'article_app/index.html', {})

class ArticleLiveListView(ListView):
    queryset = Article.objects.live()
    template_name = 'article_app/index.html'