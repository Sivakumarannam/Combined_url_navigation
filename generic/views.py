from django.shortcuts import render

# Create your views here.

def siva(request):
    return render(request,'siva.html')

def dwaraka(request):
    return render(request,'dwaraka.html')

