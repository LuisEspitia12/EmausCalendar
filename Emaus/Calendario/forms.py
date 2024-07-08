# forms.py
from django import forms
from .models import Ciudad

class SearchForm(forms.Form):
    TIPO_RETIRO_CHOICES = [
        ("Hombres", "Hombres"),
        ("Mujeres", "Mujeres"),
        ("Parejas", "Parejas"),
        ("Effeta", "Effeta"),
        ("Revolución Juvenil", "Revolución Juvenil"),
        ("Semillitas", "Semillitas"),
    ]

    tipo_retiro = forms.ChoiceField(choices=TIPO_RETIRO_CHOICES, required=False)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), required=False)
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_final = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
