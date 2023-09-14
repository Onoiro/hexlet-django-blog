from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={'who': 'world'})


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(request, 'about.html', context={'tags': tags})
