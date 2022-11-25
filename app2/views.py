from django.shortcuts import render

# Create your views here.

def a2_first(request):
    d={'a':100,'b':200}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'NANI'}
    return render(request,'a2_second.html',d)