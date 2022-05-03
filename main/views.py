from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User
from .forms import SignInForm
from django.contrib.auth import logout,login, authenticate
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password 
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
def signin(request):
   
    if request.method == "GET" :
        return render(request, 'signin.html')
   
    elif request.method == "POST":
        email = request.POST('email')
        password = request.POST('password')
        response_data = {}
        if not (email and password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."

        else : 
            User1 = User.objects.get(email=email) 
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(password, password):
                request.session['email'] = User1.id
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'signin.html',response_data)

def signout(request):
    """
    로그아웃 한 뒤 메인페이지로 이동함
    """
    logout(request)
    return HttpResponseRedirect('../')
