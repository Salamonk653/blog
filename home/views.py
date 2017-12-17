from django.shortcuts import render_to_response
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from post.models import *


# Представление сделано на основе класса View


class EIndexView(View):
    def get(self, request):
        context = {}
        # Забираем все опубликованные статье отсортировав их по дате публикации
        all_articles = Post.objects.filter(article_status=True).order_by('-created')
        # Создаём Paginator, в который передаём статьи и указываем,
        # что их будет 10 штук на одну страницу
        current_page = Paginator(all_articles, 10)

        # Pagination в django_bootstrap3 посылает запрос вот в таком виде:
        # "GET /?page=2 HTTP/1.0" 200,
        # Поэтому нужно забрать page и попытаться передать его в Paginator,
        # для нахождения страницы
        page = request.GET.get('page')
        try:
            # Если существует, то выбираем эту страницу
            context['article_lists'] = current_page.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            context['article_lists'] = current_page.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            context['article_lists'] = current_page.page(current_page.num_pages)

        return render_to_response('post/home.html', context)