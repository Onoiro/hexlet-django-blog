from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.urls import reverse


class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', args=['python', 42]))


class ArticleView(View):
    
    def get(self, request, tags, article_id):
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
