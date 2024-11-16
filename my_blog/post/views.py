from django.shortcuts import render
from .models import Author,Entry

def queries(request):
    #Obtener todos los elementos + limite
    authors = Author.objects.all()[:10]
    #Si quiero sin limites saco el [:10]

    #Obtener 10 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    #Se puede aplicar filtros:
    #filtered = Author.objects.filter(email='dustinrandolph@example.net')
    #Luego ponerlo en render, dentro de las llaves. Clase 22.

    #Obtener un único objeto
    author = Author.objects.get(id=1)

    #Listado de todas las entradas.
    entrys = Entry.objects.all()

    #Listado de todas las entradas y ordernarlos.
    orders = Author.objects.all().order_by('email')

    #Listar todos los ID <= 15.
    filtered2 = Author.objects.filter(id__lte=15)

    #Listar autores que contienen en su nombre la palabra "yes"
    filtered3 = Author.objects.filter(name__contains="yes")
    #En esta bbdd no hay ninguno.

    

    return render(request,'post/queries.html',{'authors':authors,'offsets':offsets,'orders':orders,'filtered2':filtered2,'filtered3':filtered3})
