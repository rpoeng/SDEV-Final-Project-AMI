from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def category(request, foo):
    #replace hyphens with spaces
    foo = foo.replace('-', ' ')
    #grab category from url
    try:
        #Look up category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("That Category Does Not Exist"))
        return redirect('home')


def home(request):
    products = Product.objects.all() #looks all the product model and gathers all info
    return render(request, 'home.html',{'products':products}) # Refers to the home.html in templates


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Logged In"))
            return redirect('home')
        else:
            messages.success(request, ("Invalid Username or Password"))
            return redirect('login')

    else:
        return render(request, 'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Complete"))
            return redirect('home')
        else:
            messages.success(request, ("Unable to Register, Please Try Again"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})

