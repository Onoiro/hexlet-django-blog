from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import Article
# from django.http import HttpResponse



class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html',
                              context={'articles': articles})


# class ArticleView(View):

#     def get(self, request, tags, article_id):
#         return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
