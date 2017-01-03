from users.models import Users, Countries

Users.objects.all().delete()
Countries.objects.all().delete()

user_1 = Users.objects.create(name='sergei', mail='sergei@mail.ru', login='user_1', password='qwerty123')
user_2 = Users.objects.create(name='misha', mail='misha@mail.ru', login='user_2', password='qwerty321')
user_3 = Users.objects.create(name='vitya', mail='vitya@mail.ru', login='user_3', password='ne_pridumal')

c = Countries.objects.create(name="Belarus", year=2013, user=user_1)
c.save()
c = Countries.objects.create(name="England", year=2015, user=user_2)
c.save()
c = Countries.objects.create(name="France", year=2013, user=user_3)
c.save()
