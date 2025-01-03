from django.http import HttpResponse
from django.core import render


def index(request):
    return HttpReponse('index')
    

def login(request):
    return render('login')


