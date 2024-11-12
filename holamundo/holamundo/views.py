from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo")

# poner paramétros
def adulto(request,edad):
    if edad>=18:
        return HttpResponse('Eres mayor de edad, puedes pasar!')
    else:
        return HttpResponse('No eres mayor de edad!!!')