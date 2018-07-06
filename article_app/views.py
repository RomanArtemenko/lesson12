from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Article, Category
from .forms import ArticleCreateForm, ArticleEditForm, CategoryForm


# Create your views here.
# def index(request):
#     return render(request, 'article_app/index.html', {})

class ArticleLiveListView(ListView):
    queryset = Article.objects.live()
    template_name = 'article_app/index.html'

class ArticleModerationListView(ListView):
    queryset = Article.objects.review()
    template_name = 'article_app/moderation.html'

class ArticleUserListView(ListView):
    queryset = Article.objects.review()
    template_name = 'article_app/moderation.html'

class ArticleUpdateView(UpdateView):
    form_class = ArticleEditForm
    template_name = 'article_app/add_category.html'
    success_url = 'moderation'

class ArticleCreateView(CreateView):
    form_class = ArticleCreateForm
    template_name = 'article_app/add_article.html'
    success_url = 'user-article'

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'article_app/add_category.html'
    success_url = 'xxx'
