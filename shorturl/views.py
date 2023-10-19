from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import MyShortURL

def redirectToLongURL(request,short):
    try:
        my_url = MyShortURL.objects.get(id=short)
        return redirect(my_url.longurl)
    except:
        return HttpResponse("<h1>A keresett oldal nem található!</h1>")

def returnAllURLs(request):
    li = []
    all_urls = MyShortURL.objects.all()
    for url in all_urls:
        if url.visible:
            li.append({
                "id":url.id,
                "created":url.created,
                "creator":url.creator.username,
                "title": url.title
            })
    return JsonResponse({"urls":li})
