from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect('article', kwargs={'article_id': 42, 'tags': 'python'})


def article_view(request, article_id, tags):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
