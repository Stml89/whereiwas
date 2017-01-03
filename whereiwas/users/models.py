from django.db import models

# Create your models here.


class Users(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=20)
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=20)


class Countries(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    year = models.IntegerField(default=2016)
    user = models.ForeignKey(Users)
