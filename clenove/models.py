from django.db import models

# Create your models here.

class Skaut(models.Model):
    jmeno = models.CharField("Jméno", max_length=100)
    prezdivka = models.CharField(verbose_name= "Přezdivka",
        help_text="Prosim, zadavejte bez diakritiky", 
        max_length=100)
    vek = models.IntegerField("Věk")
    splneno = models.BooleanField(default=False, help_text="Uz uplnil skautsku zkousku?")


    def __str__(self):
        return f"{self.jmeno} - {self.prezdivka}"

    class Meta:
        verbose_name_plural = "Skauti"


    