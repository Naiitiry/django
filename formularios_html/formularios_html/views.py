from django.shortcuts import render,HttpResponse

def getform(request):
    return render(request,'form.html',{})

def getgoal(request):
    if request.method != 'GET':
        return HttpResponse('El método post no está sporteadpo.')
    name = request.GET['name']
    return render(request,'success.html',{'name':name})

def postform(request):
    return render(request,'postform.html',{})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse('El método GET no está soportado.')
    info = request.POST['info']
    return render(request,'postsuccess.html',{'info':info})