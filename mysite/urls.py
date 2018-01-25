from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^complete/$', views.complete, name='complete')
]
