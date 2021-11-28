from django.contrib import admin
from django.urls import path
from .views import index, ArticleView, NewsCreateView
from django.views.generic import RedirectView


urlpatterns = [
    # path('', index, name='index'),
    path('', RedirectView.as_view(url='news/'), name='index'),
    path('news/', ArticleView.as_view(), name='articles'),
    path('news/<int:article_link>/', ArticleView.as_view(), name='article_by_link'),
    path('news/create/', NewsCreateView.as_view(), name='news_create')
]
