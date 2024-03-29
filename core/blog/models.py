from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    ARTICLE_TYPES = [
        ('UN', 'Unspecified'),
        ('TU', 'Tutorial'),
        ('RS', 'Research'),
        ('RW', 'Review'),
    ]

    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default='UN')
    categories = models.ManyToManyField(to=Category, blank=True,
                                        related_name='categories')
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    @classmethod
    def _dict_convert_article_type(cls):
        return {k: v for k, v in cls.ARTICLE_TYPES}

    def type_to_string(self):
        article_type = Article._dict_convert_article_type()
        return article_type.get(self.type)

    def __str__(self):
        return f'{self.author}: {self.title} ({self.created_datetime.date()})'
