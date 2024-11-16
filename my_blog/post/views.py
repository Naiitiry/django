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
    #entrys = Entry.objects.all()

    return render(request,'post/queries.html',{'authors':authors,'offsets':offsets})
