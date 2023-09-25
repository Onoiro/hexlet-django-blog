from django.urls import path
from .views import IndexView, ArticleView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:tags>/<int:article_id>/', ArticleView.as_view(), name='article'),
]
