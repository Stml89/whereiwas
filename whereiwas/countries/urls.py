from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^$', views.add_like),
]
