from django.http import HttpResponse
from django.core import render


def index(request):
    return HttpReponse('index')
    

def login(request):
    return render('login')


# 这是我在github上直接添加的注释和代码
def login_check(request):
    return render('/index')
    
