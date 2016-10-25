from django.conf.urls import url
from . import views

app_name = 'idea'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<idea_id>[0-9]+)/$', views.idea_details, name='idea_details'),
]