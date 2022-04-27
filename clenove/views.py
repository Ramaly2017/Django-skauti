from django.shortcuts import render
from .models import Skaut

# Create your views here.

def uvod(request):
    return render(request, "clenove/uvod.html")

def clenove(request):
    skauti_v_db = Skaut.objects.all()
    context = { "skauti_do_sablony": skauti_v_db }
    return render(request, "clenove/clenove.html", context)

def detail_clena(request, cislo):
    skaut_vysledek_dotazu_do_db = Skaut.objects.get(pk=cislo)
    return render(request, 
        "clenove/clen-detail.html", 
        { "skaut_v_sablone" : skaut_vysledek_dotazu_do_db })