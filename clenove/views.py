from django.shortcuts import render, get_object_or_404
from django.http import Http404


from .models import Skaut

# Create your views here.

def uvod(request):
    return render(request, "clenove/uvod.html")

def clenove(request):
    skauti_v_db = Skaut.objects.all()
    context = { "skauti_do_sablony": skauti_v_db }
    return render(request, "clenove/clenove.html", context)

def detail_clena(request, slug):
    # try: 
        # skaut_vysledek_dotazu_do_db = Skaut.objects.get(pk=cislo)
    # except Skaut.DoesNotExist:
        # raise Http404("Skaut se zvolenym id neexistuje.")       
    skaut_vysledek_dotazu_do_db = get_object_or_404(Skaut, slug=slug)
    context = { "skaut_v_sablone" : skaut_vysledek_dotazu_do_db }

    return render(request, "clenove/clen-detail.html", context)