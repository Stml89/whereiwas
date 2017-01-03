import os
from django.http import HttpResponse
from django.shortcuts import render_to_response


def startpage(request):
    return render_to_response('pages/main.html', {'main': True})


def open_page(request, html):
    if not os.path.exists(os.path.join(os.getcwd(), 'whereiwas', 'templates', 'pages', html)):
        return HttpResponse('404')
    else:
        return render_to_response('pages/{}'.format(html))
