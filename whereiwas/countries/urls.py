from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^article/(\d+)$', views.view_article),
    url(r'^article/addlike/(\d+)$', views.add_like),
]
