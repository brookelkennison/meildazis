from django.conf.urls import url

from . import views

app_name = 'design'
urlpatterns = [
    # ex: /design/
    url(r'^$', views.design_index, name='design_index'),
    # ex: /design/1
    url(r'^(?P<design_id>[0-9]+)/$', views.design_detail, name='design_detail'),
]
