from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User , auth
from django.http import HttpResponse
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect(loginhome)
    else:
        if request.method =='POST':
            uname = request.POST['username']
            passwd = request.POST['password']
            user= auth.authenticate(username=uname,password=passwd)
            if user is not None:
                auth.login(request, user)
                return JsonResponse('true',safe=False)
            else:
                return JsonResponse('false',safe=False)
        else:
            return render(request, 'login.html')
        
def loginhome(request):
    if request.user.is_authenticated:
        return render(request,'loginhome.html')
    else:
        return redirect(login)

    

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(login)
        
    

def signup(request):
    if request.user.is_authenticated:
        return redirect(loginhome)
    else:
        if request.method=='POST': 
            fname = request.POST['firstname']
            laname = request.POST['lastname']
            usname = request.POST['username']
            passwd = request.POST['password']
            if User.objects.filter(username=usname).exists():
                return JsonResponse('user',safe=False)
            else:
                user = User.objects.create_user(first_name=fname, last_name=laname, username=usname, password=passwd)
                user.save()
                return JsonResponse('true',safe=False)

        else:
            return render(request, 'user.html')   

def adminlogin(request):
    if request.session.has_key('password'):
        return redirect(adminhome)
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            if username=='ranjith' and password=='1234':
                request.session['password']=password
                return JsonResponse('true',safe=False)
            else:
                return JsonResponse('false',safe=False)
        else:
            return render(request, 'adminlogin.html')    

def adminhome(request):
    if request.session.has_key('password'):
        user = User.objects.all()
        return render(request, 'adminhome.html',{'user':user})
    else:
        return redirect(adminlogin)

def adminedit(request,id):
    if request.session.has_key('password'):
        if request.method=='POST':
            user=User.objects.get(id=id)
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.username= request.POST['username']
            user.save()
            return redirect(adminhome)
        else:
            user = User.objects.get(id=id)
            return render(request,'adminedit.html',{'user':user})   
    else:
        return redirect(adminlogin)
def adduser(request):
    if request.session.has_key('password'):
        if request.method=='POST':
            fname = request.POST['first_name']
            laname = request.POST['last_name']
            usname = request.POST['username']
            if User.objects.filter(username=usname).exists():
                return JsonResponse('user',safe=False)
            else:
                user = User.objects.create_user(first_name=fname, last_name=laname, username=usname)
                user.save()
                return JsonResponse('true',safe=False)
        else:
            return render(request,'useradd.html')
    else:
        return redirect(adminlogin)

def delete(request,id):
    if request.session.has_key('password'):
        user=User.objects.get(id=id)
        user.delete()
        return redirect(adminhome)
    else:
        return redirect(adminlogin)
def adminlogout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(adminlogin)

     
