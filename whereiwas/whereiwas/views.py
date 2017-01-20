from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from countries.models import Users, Articles, Countries


def start_page(request):
    users = Users.objects.all()
    for user in users:
        print(user.user_name)
        print(user.user_mail)
        print(user.user_articles.article_comments)
        print(user.user_countries.all())

    a = Articles.objects.all()
    for aa in a:
        print(aa.users_set.all())

    return render_to_response('pages/main.html', {'users': users})


def about_page(request):
    return render_to_response('pages/about.html')


# def open_page(request, html):
#     try:
#         return render_to_response('pages/{}'.format(html))
#     except ObjectDoesNotExist:
#         raise Http404
#     return redirect('pages/{}'.format(html))
