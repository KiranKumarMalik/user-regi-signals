from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def registration(request):
    EUMFO=UserForm()
    EPMFO=ProfileForm()
    d={'EUMFO':EUMFO,'EPMFO':EPMFO}

    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            #Done with User model 

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('registration is Successfull')
    

    return render(request,'registration.html',d)

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    
    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Credentials')

    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile_display(request):
    loggedInUsername=request.session.get('username')
    UO=User.objects.get(username=loggedInUsername)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'profile_display.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        loggedInUsername=request.session.get('username')
        UO=User.objects.get(username=loggedInUsername)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('ur password is changed')
    return render(request,'change_password.html')






