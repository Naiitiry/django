from django.shortcuts import render,HttpResponse, redirect 
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def index(request,letter=None):
    alphabet = ['A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith=letter.lower())
    else:
        contacts=Contact.objects.filter(name__icontains=request.GET.get('search',''))
    context = {
        'contacts':contacts,
        'alphabet':alphabet,
    }
    return render(request,'contact/index.html', context)

def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact':contact
    }
    return render(request,'contact/detail.html',context)

def edit(request, id):
    contact=Contact.objects.get(id=id)
    if request.method=='GET':
        form=ContactForm(instance=contact)
        context={
            'form':form,
            'id':id
        }
        return render(request,'contact/edit.html',context)
    if request.method=='POST':
        form=ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        context={
            'form':form,
            'id':id
        }
        messages.success(request, "Contacto actualizado.")
        return render(request,'contact/edit.html',context)
    
def create(request):
    if request.method=='GET':
        form=ContactForm()
        context={
            'form':form
        }
        return render(request,'contact/create.html',context)
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')

def delete(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')