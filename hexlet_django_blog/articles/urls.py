from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:tags>/<int:article_id>/', IndexView.as_view(), name='article')
]
