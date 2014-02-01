
from django import forms
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    content = models.TextField()

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
