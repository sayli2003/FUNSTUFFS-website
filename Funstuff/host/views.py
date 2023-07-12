from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyModelForm

# Create your views here.
def log(request):
    if request.method == 'POST':
        name=request.POST['username']
        password=request.POST['pass']

        print(name)
        print(password)

        user_obj=authenticate(username=name, password=password)
        login(request,user_obj)
        return redirect("/host/dash/")
        
    return render(request,'loginindex.html')

# @login_required
def dash(request):
    if request.user.is_authenticated:
        # User is authenticated
        context={}
        context["name"]=request.user.username
        return render(request,"starter.html",context)
    else:
        # User is not authenticated
        return redirect("/host/login/")
    
def addartwork(request):
    if request.user.is_authenticated:
        # User is authenticated
        context={}
        context["name"]=request.user.username
        context["form"]=MyModelForm()
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request,"addform.html",context)
    else:
        # User is not authenticated
        return redirect("/host/login/")
