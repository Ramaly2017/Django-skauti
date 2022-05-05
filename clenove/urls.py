from django.urls import URLPattern, path

from . import views


urlpatterns = [
    path("", views.uvod, name = "uvod"),
    path("clenove/", views.clenove, name = "clenove"),
    path("clenove/<slug:slug>", views.detail_clena, name="detail_clena")
]
