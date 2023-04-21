from django import forms
from .models import *

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ['DeptoId','DeptoNombre']
        labels = {'DeptoId':'Código de departamento',
                  'DeptoNombre':'Nombre de Departemanto'
                  }
        widgets = {'DeptoId':forms.TextInput(attrs={'class':'form-control'}),
                   'DeptoNombre':forms.TextInput(attrs={'class':'form-control'})
                  }



class Puestos(forms.ModelForm):
    class Meta:
        model= Puestos
        fields = ['puestoId','puestoNombre']
