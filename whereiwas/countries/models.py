from django.db import models

# Create your models here.


class Countries(models.Model):
    def __str__(self):
        return self.countries_name

    countries_name = models.CharField(max_length=30)
    year = models.IntegerField(default=2016)


class Comments(models.Model):
    def __str__(self):
        return self.comment_text

    comment_text = models.CharField(max_length=200)


class Articles(models.Model):
    def __str__(self):
        return self.article_title

    article_title = models.CharField(max_length=50)
    article_text = models.CharField(max_length=4000)
    article_date = models.DateTimeField(auto_now_add=True)
    article_likes = models.IntegerField(default=0)
    article_pict = models.ImageField(max_length=200)
    article_comments = models.ForeignKey(Comments)


class Users(models.Model):
    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=30)
    user_mail = models.EmailField(max_length=20)
    user_login = models.CharField(max_length=10)
    user_password = models.CharField(max_length=20)
    user_articles = models.ForeignKey(Articles, null=True)
    user_countries = models.ManyToManyField(Countries)
