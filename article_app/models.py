from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class ArticleManager(models.Manager):
    def live(self):
        return super().get_queryset().filter(state=Article.STATE_LIVE).order_by('timestamp_create')

    def review(self):
        return super().get_queryset().filter(state=Article.STATE_REVIEW).order_by('timestamp_create')

    def canceled(self):
        return super().get_queryset().filter(state=Article.STATE_CANCELED).order_by('timestamp_create')
        
class Article(models.Model):
    STATE_REVIEW = 0
    STATE_CANCELED = 25
    STATE_LIVE = 100 
    CHOICE_STATE = (
        (STATE_REVIEW, 'На модерации'),
        (STATE_LIVE, 'Опубликована'),
        (STATE_CANCELED, 'Отклонена'),
    )
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='articles')
    header = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    state = models.SmallIntegerField(choices=CHOICE_STATE, default=STATE_REVIEW)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='articles')
    timestamp_create = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)

    objects = ArticleManager()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'   
    
    def __str__(self):
        return self.header