from django.conf.urls import url

from .views import *

app_name = 'search'
urlpatterns = [
    url(r'^$', Search.as_view()),
    url(r'^1$', SearchTag.as_view()),
    url(r'^hashtag.json$', TagJson.as_view()),
]