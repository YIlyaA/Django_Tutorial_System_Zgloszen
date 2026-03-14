from django.shortcuts import get_object_or_404, redirect, render

from .forms import ZgloszenieForm
from .models import Zgloszenie


def lista_zgloszen(request):
    zgloszenia = Zgloszenie.objects.all().order_by("-data_utworzenia")
    return render(
        request,
        "zgloszenia/lista_zgloszen.html",
        {"zgloszenia": zgloszenia},
    )


def dodaj_zgloszenie(request):
    if request.method == "POST":
        form = ZgloszenieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("zgloszenia:lista_zgloszen")
    else:
        form = ZgloszenieForm()

    return render(
        request,
        "zgloszenia/formularz_zgloszenia.html",
        {
            "form": form,
            "tytul": "Dodaj zgłoszenie",
            "tekst_przycisku": "Zapisz zgłoszenie",
        },
    )


def edytuj_zgloszenie(request, pk):
    zgloszenie = get_object_or_404(Zgloszenie, pk=pk)

    if request.method == "POST":
        form = ZgloszenieForm(request.POST, instance=zgloszenie)
        if form.is_valid():
            form.save()
            return redirect("zgloszenia:lista_zgloszen")
    else:
        form = ZgloszenieForm(instance=zgloszenie)

    return render(
        request,
        "zgloszenia/formularz_zgloszenia.html",
        {
            "form": form,
            "tytul": "Edytuj zgłoszenie",
            "tekst_przycisku": "Zapisz zmiany",
        },
    )


def usun_zgloszenie(request, pk):
    zgloszenie = get_object_or_404(Zgloszenie, pk=pk)

    if request.method == "POST":
        zgloszenie.delete()
        return redirect("zgloszenia:lista_zgloszen")

    return render(
        request,
        "zgloszenia/potwierdz_usuniecie.html",
        {"zgloszenie": zgloszenie},
    )