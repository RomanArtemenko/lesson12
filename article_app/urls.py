from django.urls import path

from . import views
from .views import ArticleLiveListView

urlpatterns = [
    path('', ArticleLiveListView.as_view(), name='index'),
    #Category
    path('/category', ArticleLiveListView.as_view(), name='category-list'),
    path('/category/add', ArticleLiveListView.as_view(), name='category-add'),
    #Article
    path('/artycle', ArticleLiveListView.as_view(), name='article-list'),
    path('/article/add', ArticleLiveListView.as_view(), name='article-add'),
    path('/article/moderation', ArticleLiveListView.as_view(), name='article-moderation'),
    path('/article/<int:article_id>/detail', ArticleLiveListView.as_view(), name='article-detail'),
    path('/article/my', ArticleLiveListView.as_view(), name='article-my'),
]