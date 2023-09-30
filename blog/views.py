from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponse

def index(requests):
    return render(requests, "blog/index.html", {})


def categories(requests, numberid):
    return HttpResponse(f'<h1>page{numberid}</h1>')

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>Страница кар ца йо!</h1>")

def categ(request, catid):
    print(request.GET, "<<<")
    return HttpResponse(f"<h1>page{catid}</h1>")


