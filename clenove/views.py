from django.shortcuts import render

# Create your views here.

def uvod(request):
    return render(request, "clenove/uvod.html")

def clenove(request):
    return render(request, "clenove/clenove.html")

def detail_clena(request, cislo):
    return render(request, "clenove/clen-detail.html")