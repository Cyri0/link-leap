from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyShortURL
# Create your views here.

def redirectToLongURL(request,short):
    try:
        my_url = MyShortURL.objects.get(id=short)
        return redirect(my_url.longurl)
    except:
        return HttpResponse("<h1>A keresett oldal nem található!</h1>")