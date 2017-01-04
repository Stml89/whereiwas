import datetime.datetime
from users.models import Users, Countries, Articles, Comments

Users.objects.all().delete()
Countries.objects.all().delete()
Articles.objects.all().delete()
Comments.objects.all().delete()

user_1 = Users.objects.create(name='sergei', mail='sergei@mail.ru', login='user_1', password='qwerty123')
user_2 = Users.objects.create(name='misha', mail='misha@mail.ru', login='user_2', password='qwerty321')
user_3 = Users.objects.create(name='vitya', mail='vitya@mail.ru', login='user_3', password='ne_pridumal')

article_1 = Articles.objects.create(article_title='Title1', article_text='article_text1', article_user=user_1,
                                    article_date=datetime.datetime.now(), article_likes='0', article_pict='spain.jpg')
article_2 = Articles.objects.create(article_title='Title2', article_text='article_text2', article_user=user_2,
                                    article_date=datetime.datetime.now(), article_likes='0', article_pict='spain-terrace.jpg')

comment_1 = Comments.objects.create(comment_text='LOL', comment_article=article_1, comment_user=user_1)
comment_2 = Comments.objects.create(comment_text='WOW', comment_article=article_2, comment_user=user_2)
comment_3 = Comments.objects.create(comment_text='=)', comment_article=article_1, comment_user=user_3)

countries_1 = Countries.objects.create(name="Belarus", year=2013, user=user_1)
countries_2 = Countries.objects.create(name="England", year=2015, user=user_2)
countries_3 = Countries.objects.create(name="France", year=2013, user=user_3)
