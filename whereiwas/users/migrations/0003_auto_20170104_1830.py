# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_countries_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=50)),
                ('article_text', models.CharField(max_length=200)),
                ('article_date', models.DateTimeField()),
                ('article_likes', models.IntegerField(default=0)),
                ('article_pict', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=200)),
                ('comment_article', models.ForeignKey(to='users.Articles')),
            ],
        ),
        migrations.RenameField(
            model_name='countries',
            old_name='name',
            new_name='countries_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='login',
            new_name='user_login',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='mail',
            new_name='user_mail',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='password',
            new_name='user_password',
        ),
        migrations.AddField(
            model_name='articles',
            name='article_user',
            field=models.ForeignKey(to='users.Users'),
        ),
    ]
