from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

from .models import *
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User Created!!! ')
            return redirect('login_view')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                messages.success(request, 'You login successfully!!! ')
                return redirect('home')
            elif user is not None and user.is_employee:
                login(request, user)
                messages.success(request, 'You login successfully!!! ')
                return redirect('home')
            else:
                messages.info(request, 'error validating form')
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

def home(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, "homepage.html", context)


def products(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, "shop.html", context)


def selected_product(request, product_name):
    selected_product = Products.objects.get(slug=product_name)
    return render(request, "shop-single.html", {'selected_product': selected_product})


def search(request):
    product = request.GET['query']
    selected_product = Products.objects.get(name=product)
    return render(request, "shop-single.html", {'selected_product': selected_product})

