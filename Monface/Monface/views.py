
from django.shortcuts import render , redirect
from Monface.forms import LoginForm


def login(request):
    if len(request.POST) > 0 :
        form= LoginForm(request.POST)
        if form.is_valid() :
            return redirect('/welcome') 
        else :
            return render(request,'login.html',{'form':form})
    else :
        loginform=LoginForm()
        return render(request,'login.html',{'form':loginform})
def register(request):
    return render(request, 'register.html')

def welcome(request):
    return render(request,'welcome.html')