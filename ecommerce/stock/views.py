from django.shortcuts import render,HttpResponse
from .forms import ProductsForm

def index(request):
    if request.method=='POST':
        form=ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html',{'form':form})
    else:
        form = ProductsForm()
        return render(request,'index.html',{'form':form})
