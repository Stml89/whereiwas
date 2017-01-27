from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main-page'),
    url(r'about$', views.about, name='about-page'),
    url(r'^article/add_like/(\d+)', views.add_like),
    url(r'^article/add_article', views.add_article, name="add-article"),
    url(r'countries/article/(\d+)/delete_comment', views.delete_comment),
    url(r'countries/article/(\d+)/delete_article', views.delete_article),
    url(r'^countries/article/(.*)$', views.view_article, name='article-page'),
    url(r'login_user', views.user_login, name='login-page'),
    url(r'logout', views.user_logout, name='logout-page'),
    url(r'search', views.search, name='search-page'),
    url(r'user_profile/', views.user_profile, name='user-profile-page'),
]
