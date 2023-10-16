from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.forms import ModelForm
from django.contrib import messages
from .models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html',
                      context={'articles': articles})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html',
                      context={'article': article})


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) < 2:
            self.add_error('name',
                           'Title should be no less than 2 characters')
        if len(data) > 20:
            self.add_error('name',
                           'Title should be no longer 20 characters')
        return data

    def clean_body(self):
        data = self.cleaned_data['body']
        if len(data) < 2:
            self.add_error('body',
                           'Article should be no less than 2 characters')
        if len(data) > 2000:
            self.add_error('body',
                           'Article should be no longer 2000 characters')
        return data


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article was added successfully')
            return redirect('index')
        messages.error(request, 'Error when adding an article')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html',
                      {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article was updated successfully')
            return redirect('index')
        messages.error(request, 'Error when update an article')
        return render(request, 'articles/update.html',
                      {'form': form, 'article_id': article_id})
