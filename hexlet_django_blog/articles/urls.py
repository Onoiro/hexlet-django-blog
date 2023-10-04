from django.urls import path
from .views import IndexView, ArticleView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:id>/', ArticleView.as_view(), name='article_view')
]
