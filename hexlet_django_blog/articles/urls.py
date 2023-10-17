from django.urls import path
from .views import IndexView, ArticleView, \
                   ArticleFormCreateView, \
                   ArticleFormEditView, \
                   ArticleFormDeleteView


urlpatterns = [
     path('', IndexView.as_view(),
          name='index'),
     path('<int:id>/edit/', ArticleFormEditView.as_view(),
          name='articles_update'),
     path('<int:id>/delete/', ArticleFormDeleteView.as_view(),
          name='articles_delete'),
     path('<int:id>/', ArticleView.as_view(),
          name='article_view'),
     path('create/', ArticleFormCreateView.as_view(),
          name='articles_create'),
]
