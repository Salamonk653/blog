from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^post/(?P<id>\w+)/$', views.post_single, name='post_single'),
    url(r'^$', views.EIndexView.as_view(), name='index'),
    # url(r'^search/$', views.PostListViews.as_view(), name='search'),
]