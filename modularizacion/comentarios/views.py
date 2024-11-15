from django.shortcuts import render, HttpResponse
from .models import Comentarios

# Create your views here.
def test(request):
    return HttpResponse('Esto es un test.')

def create(request):
    """comentario = Comentarios(
        name='Juanjo',
        score = 5,
        comment = "Esto es un comentario."
    )"""
    comentario = Comentarios(name='Alex')
    comentario.save()
    return HttpResponse("Ruta para creación de modelos.")


def delete(request):
    """comentario = Comentarios.objects.get(id=2)
    comentario.delete()"""
    Comentarios.objects.filter(id=1).delete()
    return HttpResponse('Ruta para eliminar comentarios.')
