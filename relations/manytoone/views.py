from django.shortcuts import render,HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='Alan',last_name='Pert',email='alpe@gmail.com')
    rep.save()

    art1 = Article(headline='Los carabajal',pub_date=date(2022,5,5), reporter=rep)
    art2 = Article(headline='Lorem ipsum oqof',pub_date=date(2022,6,26), reporter=rep)
    art3 = Article(headline='Vicitudes de la vida',pub_date=date(2020,11,7), reporter=rep)

    art1.save()
    art2.save()
    art3.save()

    #query = art1.reporter.first_name
    result = rep.article_set.all()

    return HttpResponse(result)

