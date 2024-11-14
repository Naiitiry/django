from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def muestra(request):
    return render(request,'muestra.html',{})