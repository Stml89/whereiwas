from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist


def startpage(request):
    return render_to_response('pages/main.html', {'main': True})


def open_page(request, html):
    try:
        return render_to_response('pages/{}'.format(html))
    except ObjectDoesNotExist:
        raise Http404
    return redirect('pages/{}'.format(html))
