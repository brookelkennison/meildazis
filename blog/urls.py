from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    url(r'^$', views.blog_index, name='blog_index'),
    # ex: /blog/1
    url(r'^(?P<post_id>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    # category
    url(r'^(?P<category>[0-9]+)/$', views.blog_category, name="blog_category"),
]

