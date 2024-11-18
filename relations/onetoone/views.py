from django.shortcuts import render,HttpResponse
from .models import Place, Restaurant


def create(request):
    place = Place(name='Lugar 1', addres='Calle Demo')
    place.save()

    restaurant = Restaurant(place=place, number_of_employee=8)
    restaurant.save()

    return HttpResponse(restaurant.place.addres)
