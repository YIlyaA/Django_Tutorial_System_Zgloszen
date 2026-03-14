from django.urls import path

from . import views

app_name = "zgloszenia"

urlpatterns = [
    path("", views.lista_zgloszen, name="lista_zgloszen"),
    path("dodaj/", views.dodaj_zgloszenie, name="dodaj_zgloszenie"),
    path("edytuj/<int:pk>/", views.edytuj_zgloszenie, name="edytuj_zgloszenie"),
    path("usun/<int:pk>/", views.usun_zgloszenie, name="usun_zgloszenie"),
]
