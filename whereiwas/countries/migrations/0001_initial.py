# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50)),
                ('article_text', models.CharField(max_length=4000)),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('article_likes', models.IntegerField(default=0)),
                ('article_pict', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries_name', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=2016)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_mail', models.EmailField(max_length=20)),
                ('user_login', models.CharField(max_length=10)),
                ('user_password', models.CharField(max_length=20)),
                ('user_articles', models.ManyToManyField(to='countries.Articles')),
                ('user_countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.Countries')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='article_comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.Comments'),
        ),
    ]