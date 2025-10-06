from django.shortcuts import render

# Create your views here.

from .models import *


def home(request):
    return render(request, 'home.html',{'name':'Veda'})


def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])

    val3=val1+val2

    return render(request,'result.html',{'result':val3})

def dashboard(request):
    customer=Customer.objects.all()
    return render(request,'dashboard.html',{'customer':customer})


def product(request):
    prod=Product.objects.all()
    return render(request,'product.html',{'product':prod})