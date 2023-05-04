from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('ja existe um usuario com esse username')
        
        user = User.objects.create_user(username=username, email = email, password=password)
        user.save()

        return HttpResponse('usuario cadastrado com sucesso')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('usuario ou senha invalidos')

@login_required(login_url="/auth/login/")
def plataforma(request):
        return HttpResponse('plataforma logado')
