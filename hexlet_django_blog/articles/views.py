from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        # return render(request, 'articles/article.html', context = {'title': 'Article'})
        return redirect('article', kwargs={'article_id': 42, 'tags': 'python'}) 


def article_view(request):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
