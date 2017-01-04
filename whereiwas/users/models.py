from django.db import models

# Create your models here.


class Users(models.Model):
    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=30)
    user_mail = models.EmailField(max_length=20)
    user_login = models.CharField(max_length=10)
    user_password = models.CharField(max_length=20)


class Countries(models.Model):
    def __str__(self):
        return self.countries_name

    countries_name = models.CharField(max_length=30)
    year = models.IntegerField(default=2016)
    user = models.ForeignKey(Users)


class Articles(models.Model):
    def __str__(self):
        return self.article_title

    article_title = models.CharField(max_length=50)
    article_text = models.CharField(max_length=200)
    article_user = models.ForeignKey(Users)
    article_date = models.DateTimeField(auto_now_add=True)
    article_likes = models.IntegerField(default=0)
    article_pict = models.CharField(max_length=200)


class Comments(models.Model):
    def __str__(self):
        return self.comment_text

    comment_text = models.CharField(max_length=200)
    comment_article = models.ManyToManyField(Articles)
    comment_user = models.ForeignKey(Users)
