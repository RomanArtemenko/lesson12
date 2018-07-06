from django import forms
from .views import Article, Category

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['header', 'text', 'category_id']

class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['header', 'text', 'category_id', 'state']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']