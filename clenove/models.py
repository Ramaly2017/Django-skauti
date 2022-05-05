from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class AdresaKlubovny(models.Model):
    ulice = models.CharField(max_length=100)
    cislo_popisne = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Adresy Kluboven"
    
    def __str__(self):
        return f"{self.ulice} {self.cislo_popisne}"
       


class Oddil(models.Model):
    jmeno = models.CharField("jmeno", max_length=100)
    heslo = models.CharField(max_length=300)
    klubovna = models.OneToOneField(AdresaKlubovny, on_delete=models.SET_NULL, null=True)

    def seznam_skautu(self):
        return [skaut.jmeno for skaut in self.skauti.all()]

    class Meta:
        verbose_name_plural = "Oddily"
        verbose_name = "Oddil"

    def __str__(self):
        return self.jmeno

class Bobrik(models.Model):
    nazev = models.CharField(max_length=100)
    barva = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Bobrici"
        
    def __str__(self):
        return self.nazev


class Skaut(models.Model):
    jmeno = models.CharField("Jméno", max_length=100)
    prezdivka = models.CharField(verbose_name= "Přezdivka",
        help_text="Prosim, zadavejte bez diakritiky", 
        max_length=100)
    vek = models.IntegerField("Věk")
    slug = models.SlugField()
    splneno = models.BooleanField(default=False, help_text="Uz uplnil skautsku zkousku?")
    oddil = models.ForeignKey(Oddil, verbose_name="Oddil", on_delete=models.CASCADE, related_name = "skauti")
    bobrici = models.ManyToManyField(Bobrik, null=True, related_name = "skauti")

    def get_absolute_url(self):
        return reverse("detail_clena", args=[self.slug])

    # def save(self, *args, **kwargs):
        # self.slug = slugify(self.prezdivka)
        # print("Ukladam do db")
        # super().save(*args, **kwargs)  

    def __str__(self):
        return f"{self.jmeno} - {self.prezdivka}"

    class Meta:
        verbose_name_plural = "Skauti"


    