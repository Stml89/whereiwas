from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.
def test(request):
    return render_to_response('users/index.html')


def add_like(request):
    return render_to_response('users/index.html')
