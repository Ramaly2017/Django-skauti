from django.urls import URLPattern, path

from . import views


urlpatterns = [
    path("", views.uvod),
    path("clenove", views.clenove),
    path("clenove/<int:cislo>", views.detail_clena)
]
