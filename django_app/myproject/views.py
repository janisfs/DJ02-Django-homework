from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'myproject/index.html')

def page1(request):
    return render(request, 'myproject/page1.html')

def page2(request):
    return render(request, 'myproject/page2.html')

def page3(request):
    return render(request, 'myproject/page3.html')

def page4(request):
    return render(request, 'myproject/page4.html')
