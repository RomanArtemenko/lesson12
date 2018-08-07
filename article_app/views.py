from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Article, Category
from django.contrib.auth.models import User
from .forms import ArticleCreateForm, ArticleEditForm, CategoryForm


# Create your views here.
# def index(request):
#     return render(request, 'article_app/index.html', {})

class ArticleLiveListView(ListView):
    queryset = Article.objects.live()
    template_name = 'article_app/index.html'

class ArticleModerationListView(ListView):
    queryset = Article.objects.review()
    template_name = 'article_app/moderation_article.html'

class ArticleUserListView(ListView):
    queryset = Article.objects.owner(1)
    template_name = 'article_app/my_article.html'

class ArticleUpdateView(UpdateView):
    form_class = ArticleEditForm
    template_name = 'article_app/edit_article.html'
    success_url = reverse_lazy('article-moderation')

class ArticleCreateView(CreateView):
    form_class = ArticleCreateForm
    template_name = 'article_app/add_article.html'
    success_url = reverse_lazy('article-user')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'article_app/add_category.html'
    success_url = reverse_lazy('category-list')

class CategoryListView(ListView):
    template_name = 'article_app/category.html'
    model = Category 

class SignInView(View):
    pass

class SignUpView(View):
    pass

class SignOutView(View):
    pass
