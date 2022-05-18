from collections import UserString
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password 
from .models import User

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method =='GET':
        return render(request,'signup.html')

    elif request.method =='POST':
        email = request.POST.get('email','')
        nickname = request.POST.get('nickname','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')
        if(email or nickname or password1 or password2) =='':
            return redirect('../signup/')
        elif password1 != password2:
            return redirect('../signup/')
        else:
            user = User(
                email = email,
                password = password1,
                nickname = nickname,
            )
            user.save()
        return redirect('../signin/')
# def signin(request):
#     if request.method == 'POST':
#         # login.html에서 넘어온 email과 password를 각 변수에 저장하기.
#         username = request.POST['email']
#         password = request.POST['password']
#         # 해당 email과 password와 일치하는 user 객체를 가져온다.

#         user = authenticate(request, username=username, password=password)
#         print(user)
#         # 해당 user 객체가 존재한다면(객체가 존재하지 않는다면 none을 반환할 텐데, none이 not이니까 존재한다면!)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('index')
#         else:
#             return render(request, 'signin.html', {'error': 'signin or password is incorrect.'})
#     else:
#         return render(request, 'signin.html')

def signin(request):
    if request.method == 'POST':
#         # login.html에서 넘어온 email과 password를 각 변수에 저장하기.
        username = request.POST['email']
        password = request.POST['password']
        me = User.objects.get(email = username)
        user = authenticate(request, username=username, password=password)
        if me.password == password:
            login(request, user)
            return redirect('index')
        else :
            return render(request, 'signin.html')
    else :
         return render(request, 'signin.html')






def signout(request):
    """
    로그아웃 한 뒤 메인페이지로 이동함
    """
    logout(request)
    return redirect("index")
