from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import ImageForm,signupForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Image
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        post = User.objects.all()
        user = request.user
        full_name = user.get_full_name()
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        form = ImageForm()
        img = Image.objects.all()
        return render(request, 'myapp/home.html', {'img':img,'form':form ,'full_name':full_name})

    else:
        return HttpResponseRedirect('/login/')

#signup
def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = signupForm()

    return render(request, 'myapp/signup.html', {'form':form})
   
#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
        else:
            form = LoginForm()
        return render(request, 'myapp/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')