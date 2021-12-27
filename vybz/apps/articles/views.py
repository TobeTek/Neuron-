from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.


class ArticleListView(generic.ListView):
    model = models.Article
    template_name =  "articles/index.html"
    