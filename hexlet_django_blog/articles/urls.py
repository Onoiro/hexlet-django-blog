from django.urls import path
from .views import IndexView, article_view


urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:tags>/<int:article_id>/', article_view, name='article')
]
