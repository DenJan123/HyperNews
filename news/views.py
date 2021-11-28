from django.shortcuts import render, redirect
from django.views import View
from . import utils
from itertools import groupby
import random
from datetime import datetime


# Create your views here.

def index(request):
    return render(request, 'news/layout.html')


class ArticleView(View):


    def get(self, request, *args, **kwargs):
        articles = utils.read_json_data()
        if kwargs.get('article_link'):
            articles_dict = {article['link']: article for article in articles}
            if kwargs.get('article_link') in articles_dict:
                return render(request, 'news/article.html', context={
                    'article': articles_dict.get(kwargs.get('article_link'))
                })
        articles = sorted(articles, key=lambda article: article['created'], reverse=True)
        articles_dict = dict()
        query = ''
        if len(request.GET) > 0:
            query = request.GET.get('q')
        for article in articles:
            if query and not (query in article['title']):
                continue
            if article['created'][:10] in articles_dict:
                articles_dict[article['created'][:10]].append(article)
            else:
                articles_dict[article['created'][:10]] = [article]

        # articles_dict = {key: list(group) for key, group
        #                  in groupby(articles, key=lambda x: x["created"][:10])}

        return render(request, 'news/articles.html', context={
            'articles_by_dates': articles_dict
        })


class NewsCreateView(View):


    def get(self, request, *args, **kwargs):
        return render(request, 'news/news_create.html', context={
            'form': utils.NewsCreateForm()
        })


    def post(self, request, *args, **kwargs):
        form = utils.NewsCreateForm(request.POST)
        if form.is_valid():
            articles = utils.read_json_data()
            links = [article['link'] for article in articles]
            random_link = random.choice(list(set(range(min(links)+1, max(links)))-set(links)))
            created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            article = {'created': created}
            article.update(form.cleaned_data)
            article['link'] = random_link
            articles.append(article)
            utils.save_json_data(articles)
        return redirect('/news/')
