from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models2 import *


class ModuloUno(forms.ModelForm):
    class Meta:
        print("LLEGO AL FORMULARIO")
        model = PrimerModulo
        exclude = ['timestamp']


class ModuloDurante(forms.ModelForm):
    class Meta:
        print("LLEGO AL FORMULARIO")
        model = ModuloDuranteUno
        exclude = ['timestamp']

class ModuloDuranteCore(forms.ModelForm):
    class Meta:
        print("LLEGO AL FORMULARIO")
        model = ModuloDuranteDos
        exclude = ['timestamp']


class ModuloDuranteCoreTres(forms.ModelForm):
    class Meta:
        print("LLEGO AL FORMULARIO")
        model = ModuloDuranteTres
        exclude = ['timestamp']


class ModuloDuranteCoreCuatro(forms.ModelForm):
    class Meta:
        print("LLEGO AL FORMULARIO")
        model = ModuloDuranteCuatro
        exclude = ['timestamp']

class ModuloDuranteCoreCinco(forms.ModelForm):
    class Meta:
        print("LLEGO AL FORMULARIO")
        model = ModuloDuranteCinco
        exclude = ['timestamp']


class ModuloDuranteCoreFinal(forms.ModelForm):
    class Meta:
        print("LLEGO AL FORMULARIO")
        model = Final
        exclude = ['timestamp']


