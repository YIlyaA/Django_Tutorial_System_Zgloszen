from django.db import models


class Zgloszenie(models.Model):
    imie_nazwisko = models.CharField(max_length=100, verbose_name="Imię i nazwisko")
    email = models.EmailField(verbose_name="Adres e-mail")
    temat = models.CharField(max_length=150, verbose_name="Temat zgłoszenia")
    tresc = models.TextField(verbose_name="Treść zgłoszenia")
    data_utworzenia = models.DateTimeField(
        auto_now_add=True, verbose_name="Data utworzenia"
    )

    class Meta:
        verbose_name = "Zgłoszenie"
        verbose_name_plural = "Zgłoszenia"

    def __str__(self):
        return f"{self.temat} - {self.imie_nazwisko}"
