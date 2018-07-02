from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Article(models.Model):
    CHOICE_STATE = (
        ('REVIEW', 'На модерации'),
        ('LIVE', 'Опубликована'),
        ('CANCELED', 'Отклонена'),
    )
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=1024)
    state = models.CharField(choice=CHOICE_STATE, default='REVIEW')
    timestamp_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'   
    
    def __str__(self):
        return self.header