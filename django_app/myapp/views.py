from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def page1(request):
    return render(request, 'myapp/page1.html')

def page2(request):
    return render(request, 'myapp/page2.html')

def page3(request):
    return render(request, 'myapp/page3.html')

def page4(request):
    return render(request, 'myapp/page4.html')
