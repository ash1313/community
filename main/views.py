from django.shortcuts import render, redirect
from .models import User


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
        return render(request,'signin.html')
        