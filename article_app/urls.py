from django.urls import path

from . import views
from .views import ArticleLiveListView, ArticleModerationListView, ArticleUserListView, ArticleCreateView, CategoryCreateView, CategoryListView
    
urlpatterns = [
    path('', ArticleLiveListView.as_view(), name='index'),
    #Category
    path('category', CategoryListView.as_view(), name='category-list'),
    path('category/add', CategoryCreateView.as_view(), name='category-add'),
    #Article
    path('artycle', ArticleLiveListView.as_view(), name='article-list'),
    path('article/add', ArticleCreateView.as_view(), name='article-add'),
    path('article/moderation', ArticleModerationListView.as_view(), name='article-moderation'),
    path('article/<int:article_id>/detail', ArticleLiveListView.as_view(), name='article-detail'),
    path('article/my', ArticleUserListView.as_view(), name='article-user'),
]