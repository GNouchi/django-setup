from django.conf.urls import url 
from . import views 
# this page matches the url 
urlpatterns = [
    url(r'^new', views.new),
    url(r'^create', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy),
    url(r'^', views.index),
]