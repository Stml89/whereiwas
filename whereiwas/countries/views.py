from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from countries.models import Users, Countries, Articles, Comments
from django.core.exceptions import ObjectDoesNotExist
# from forms import CommentForm
# from django.core.context_processor import csrf


def test(request):
    return render_to_response('users/index.html')


def add_like(request, article_id):
    try:
        article = Articles.object.get(id=article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('users/index.html')


def add_article(request, article_id):
    # comment_form = CommentForm
    args = dict()
    # args.update(csrf(request))
    args['article'] = Articles.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter()


def view_article(request, article_id):
    try:
        article = Articles.object.get(id=article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404

    return render_to_response('users/index.html')
