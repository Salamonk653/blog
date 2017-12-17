# -*- coding: utf-8 -*-

from django.http import HttpResponse


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = 'По запросу: ' + request.GET['q'].encode('utf-8')
    else:
        message = 'Нечего не нашел'
    return HttpResponse(message)
