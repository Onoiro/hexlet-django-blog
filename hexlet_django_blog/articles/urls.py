from django.urls import path
from .views import IndexView, ArticleView, ArticleCommentsView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:id>/', ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view())
]
