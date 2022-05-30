from collections import UserString
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password 
from .models import User
from .forms import LoginForm

def index(request):

    # login을 통해서 확인된 user는 session을 통해 user.id를 넘겨 받았다.
    user_id = request.session.get('user')
    # user_id유무를 통해 login판단
    if user_id:
        user = User.objects.get(pk=user_id)
        return render(request,'index.html')
    return HttpResponse('Home')

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

def signin(request):
    if request.method =="GET":
        return render(request,'signin.html')
    elif request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        res_data = {}
        if not(email and password):
            res_data['error'] = "모든 칸을 입락하세요"
        else:
            db = User.objects.get(email = email)
            if db.password == password:
                request.session['user'] = db.id
                return redirect('index')
            else:
                res_data['error']="비밀번호 오류"
        return render(request,'signin.html',res_data)


def signout(request):
    """
    로그아웃 한 뒤 메인페이지로 이동함
    """
    logout(request)
    return redirect("index")
