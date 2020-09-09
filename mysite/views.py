from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html',{'name':'admin'})

def about(request):
    return render(request, 'about.html',)

def login(request):
    return render(request, 'login.html',)

def result(request): 
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, 'input.html',{'result':res})