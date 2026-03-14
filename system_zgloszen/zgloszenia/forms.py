from django import forms

from .models import Zgloszenie


class ZgloszenieForm(forms.ModelForm):
    class Meta:
        model = Zgloszenie
        fields = ["imie_nazwisko", "email", "temat", "tresc"]
        widgets = {
            "imie_nazwisko": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "temat": forms.TextInput(attrs={"class": "form-control"}),
            "tresc": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
