from datetime import datetime
from django.contrib.auth.models import User
from countries.models import CountrUsers, Countries, Articles, Comments


CountrUsers.objects.all().delete()
Countries.objects.all().delete()
Articles.objects.all().delete()
Comments.objects.all().delete()


countries_1 = Countries.objects.create(countries_name="Belarus", year=2013)
countries_2 = Countries.objects.create(countries_name="England", year=2015)
countries_3 = Countries.objects.create(countries_name="France", year=2014)


comment_1 = Comments.objects.create(comment_text='lol')
comment_2 = Comments.objects.create(comment_text='wow')


article_1 = Articles.objects.create(article_title='Title1', article_text='article_text1', article_date=datetime.now(),
                                    article_likes='0', article_pict='spain.jpg', article_comments=comment_1)
article_2 = Articles.objects.create(article_title='Title2', article_text='article_text2', article_date=datetime.now(),
                                    article_likes='0', article_pict='spain-terrace.jpg', article_comments=comment_2)


user_1 = User.objects.create(user_name='sergei', user_articles=article_1, avatar='')
user_1.user_countries = [countries_1]
user_1.save()
user_2 = User.objects.create(user_name='misha', user_articles=article_2, avatar='')
user_2.user_countries = [countries_1, countries_2]
user_2.save()
user_3 = User.objects.create(user_name='vitya', user_articles=article_2, avatar='')
user_3.user_countries = [countries_2, countries_3]
user_3.save()
