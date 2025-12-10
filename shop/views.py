from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# Create your views here.
def helloworld(request):
    all_product = Product.objects.all()
    all_category = Category.objects.all()
    return render(request, 'index.html', {'products' : all_product, 'categories' : all_category})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('با موفقیت وارد شدید'))
            return redirect('main-page')
        else:
            messages.error(request, 'مشکلی در ورود است', extra_tags='danger')
            return redirect('login-page')
    else:
        return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, ('خارج شدید'))
    return redirect('main-page')

def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']        
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request,'ثبت نام با موفقیت بود')
            return redirect('main-page')
        else:
            messages.error(request, 'مشکلی در ثبت نام هست', extra_tags='danger')
            return redirect('signup-page')
    else:
        return render(request, 'signup.html', {'form': form})
    
def product(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {'product': product})

def category(request, name):
    all_category = Category.objects.all()
    category = Category.objects.get(name=name)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'categories': all_category, 'products': products})