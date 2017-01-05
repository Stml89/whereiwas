# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('article_title', models.CharField(max_length=50)),
                ('article_text', models.CharField(max_length=200)),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('article_likes', models.IntegerField(default=0)),
                ('article_pict', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('comment_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('countries_name', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=2016)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user_name', models.CharField(max_length=30)),
                ('user_mail', models.EmailField(max_length=20)),
                ('user_login', models.CharField(max_length=10)),
                ('user_password', models.CharField(max_length=20)),
                ('user_articles', models.ManyToManyField(to='users.Articles')),
                ('user_countries', models.ForeignKey(to='users.Countries')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='article_comments',
            field=models.ForeignKey(to='users.Comments'),
        ),
    ]
