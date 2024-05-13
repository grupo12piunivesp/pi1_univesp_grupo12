from django import forms
from .models import *

class DoacaoForms(forms.ModelForm):
    class Meta:
        model = Doacao_Cadastro
        fields = '__all__'

class VoluntarioForms(forms.ModelForm):
    class Meta:
        model = Voluntario_Cadastro
        fields = '__all__'
