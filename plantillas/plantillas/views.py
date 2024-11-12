from django.shortcuts import render

def simple(request):
    return render(request, "simple.html", {})

def dinamico(request,name):
    context = {'name':name}
    return render(request,'dinamico.html',context)