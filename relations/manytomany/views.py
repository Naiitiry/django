from django.shortcuts import render, HttpResponse
from .models import Article, Publication

def create(request):
    """
    art1 = Article(headline='Artículo 1')
    art1.save()
    art2 = Article(headline='Artículo 2')
    art2.save()
    art3 = Article(headline='Artículo 3')
    art3.save()

    pub1 = Publication(title='Publicación primera.')
    pub1.save()
    pub2 = Publication(title='Publicación segunda.')
    pub2.save()
    pub3 = Publication(title='Publicación tercera.')
    pub3.save()
    pub4 = Publication(title='Publicación cuarta.')
    pub4.save()
    pub5 = Publication(title='Publicación quinta.')
    pub5.save()
    pub6 = Publication(title='Publicación sexta.')
    pub6.save()
    pub7 = Publication(title='Publicación septima.')
    pub7.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)
    
    resultado = art1.publications.all()
    """
    # Para eliminar 1 relación:
    # art1.publications.remove(pub1)
    
    pub1 = Publication.objects.get(id=1)
    resultado = pub1.article_set.all()



    return HttpResponse(resultado)