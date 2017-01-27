from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Countries(models.Model):
    def __str__(self):
        return self.countries_name

    countries_name = models.CharField(max_length=30)
    year = models.IntegerField(default=2016)


class Articles(models.Model):
    def __str__(self):
        return self.article_title

    article_title = models.CharField(max_length=50)
    article_text = models.CharField(max_length=4000)
    article_date = models.DateTimeField(auto_now_add=True)
    article_likes = models.IntegerField(default=0)
    article_pict = models.ImageField(max_length=200)


class CountrUsers(models.Model):
    def __str__(self):
        return str(self.user_name)

    user_name = models.OneToOneField(User)
    user_articles = models.ForeignKey(Articles, null=True)
    user_countries = models.ManyToManyField(Countries)
    avatar = models.ImageField(max_length=200)


class Comments(models.Model):
    def __str__(self):
        return self.comment_text

    comment_text = models.CharField(max_length=200)
    comment_article = models.ForeignKey(Articles, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_author = models.ManyToManyField(CountrUsers)
