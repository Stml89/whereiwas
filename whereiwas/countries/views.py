from django.http import Http404
from django.shortcuts import redirect, render
from countries.models import CountrUsers, Countries, Articles, Comments
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.db.models import Q


def main_page(request):
    users = list()
    mini_posts = list()
    if request.GET:
        if 'next' in request.GET['page']:
            data = int(request.GET['data']) + 2
            articles = Articles.objects.all().order_by('-article_date')[int(request.GET['data']):int(request.GET['data'])+2]
        else:
            data = int(request.GET['data']) - 2
            articles = Articles.objects.all().order_by('-article_date')[int(request.GET['data'])-2:int(request.GET['data'])]
    else:
        data = 2
        articles = Articles.objects.all().order_by('-article_date')[:2]

    for i in articles:
        users.append(CountrUsers.objects.filter(user_articles__article_title=i))

    articles = Articles.objects.all().order_by('-article_likes')[:4]
    for i in articles:
        mini_posts.append(CountrUsers.objects.filter(user_articles=i))

    return render(request, 'pages/main.html', {'users': users,
                                               'main': True,
                                               'data': data,
                                               'mini_posts': mini_posts})


@csrf_protect
def view_article(request, article_id):
    args = dict()
    args['article'] = Articles.objects.get(article_title=article_id)

    if request.POST:
        user = CountrUsers.objects.get(user_name__username=auth.get_user(request).username)
        c = Comments.objects.create(comment_text=request.POST['comment'], comment_date=datetime.now(),
                                    comment_article=args['article'])
        c.comment_author.add(user)
        c.save()

    args['username'] = CountrUsers.objects.get(user_articles__article_title=args['article'].article_title)
    comments = Comments.objects.filter(comment_article=args['article'])
    args['comment_count'] = len(comments)

    args['comments'] = dict()
    for i in comments:
        args['comments'].update({CountrUsers.objects.filter(comments__comment_text=i): i})

    if args['username'].user_name.username == auth.get_user(request).username:
        args['owner'] = True
    else:
        args['owner'] = False

    return render(request, 'pages/single.html', args)


def about(request):
    args = dict()
    args['about'] = True
    args['title'] = 'About'
    return render(request, 'pages/other.html', args)


@csrf_protect
def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Login failed')
            return redirect(request.GET["next"])
    else:
        return render(request, 'pages/logform.html', {'login': True, 'form_name': 'Login'})


def user_logout(request):
    auth.logout(request)
    return redirect('/')


# def user_register(request):
#     return render_to_response('pages/logform.html', {'register': True, 'form_name': 'Register'})


def add_like(request, article_id):
    article = Articles.objects.get(id=article_id)
    article.article_likes += 1
    article.save()
    return redirect('/')


@csrf_protect
def add_article(request):
    args = dict()
    args['new_article'] = True

    if request.POST:
        args['year'] = request.POST['year']
        args['country'] = request.POST['country']
        args['title'] = request.POST['title']
        args['story'] = request.POST['story']
        args['image'] = request.POST['image']

        print(auth.get_user(request).username)
        cuser = CountrUsers.objects.get(user_name__username=auth.get_user(request).username)

        try:
            CountrUsers.objects.get(user_countries__countries_name=request.POST['country'])
        except CountrUsers.DoesNotExist:
            c = Countries.objects.create(countries_name=args['country'], year=args['year'])
            c.save()

        try:
            Articles.objects.get(article_title=request.POST['title'])
        except Articles.DoesNotExist:
            a = Articles.objects.create(article_title=args['title'],
                                        article_text=args['story'],
                                        article_date=datetime.now(),
                                        article_likes=0,
                                        article_pict=args['image'])
        cuser.user_countries.add(c)
        cuser.user_articles = a
        cuser.save()
        a.save()

        return redirect("/")
    else:
        return render(request, 'pages/single.html', args)


def delete_comment(request, pk):
    Comments.objects.get(pk=pk).delete()
    return redirect(request.GET["next"])


def delete_article(request, pk):
    Articles.objects.get(pk=pk).delete()
    return redirect("/")


def search(request):
    args = dict()
    args['title'] = 'Search result'
    args['articles'] = Articles.objects.filter(Q(article_title__contains=request.GET['query']) |
                                              Q(article_text__contains=request.GET['query']))

    return render(request, 'pages/other.html', args)


def user_profile(request):
    args = dict()
    args['user'] = CountrUsers.objects.get(pk=request.GET['user_id'])
    args['countries'] = Countries.objects.filter(countrusers__user_name__username=args['user'])

    return render(request, 'pages/other.html', args)
