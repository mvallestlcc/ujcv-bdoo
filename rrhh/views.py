'''
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Expediente
def expediente_index(request):
    return HttpResponse("Cargando vistas")
    
def expediente_index2(request):

    context = {
         'primerNombre':"Francisco",
         'primerApellido':"Morazán",
         'edad':56, 
    }
    return render(request, 'expediente/index.html', context)

def expediente_index3(request):

    expediente =  Expediente.objects.only('nombre', 'apellido', 'identidad')
    context = {'expedientes':expediente}
    return render(request, 'expediente/index.html', context)
'''

from django.views import generic
from  .models import *
from django.urls import reverse_lazy
from .forms import DepartamentoForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class departamentoListar(LoginRequiredMixin, generic.ListView):
    template_name = 'departamentos/index.html'
    model = Departamentos
    context_object_name = "departamentos"
    login_url = '/login'

class departamentoAgregar(LoginRequiredMixin, generic.CreateView):
    model = Departamentos
    form_class = DepartamentoForm
    template_name = 'departamentos/agregar.html' 
    success_url = reverse_lazy('departamentos_listar')
    login_url = '/login'

class departamentosEditar(LoginRequiredMixin, generic.UpdateView):
    model= Departamentos
    form_class = DepartamentoForm
    context_object_name = "departamentos"
    template_name = 'departamentos/agregar.html'
    success_url = reverse_lazy('departamentos_listar')
    login_url = '/login'

class departamentosEliminar(LoginRequiredMixin, generic.DeleteView):
    model= Departamentos
    form_class = DepartamentoForm
    context_object_name = "departamentos"
    template_name = 'departamentos/eliminar.html'
    success_url = reverse_lazy('departamentos_listar')
    login_url = '/login'

'''

class puestoListar(generic.ListView):
    template_name = 'puestos/index.html'
    model = Puestos
    context_object_name = "puestos"

class puestosAgregar(generic.CreateView):
    model = Puestos
   # form_class = PuestoForm
    template_name = 'puestos/agregar.html' 
    success_url = reverse_lazy('puestos_listar')

class puestosEditar(generic.UpdateView):
    model = Puestos
    #form_class = PuestoForm
    template_name = 'puestos/agregar.html' 
    success_url = reverse_lazy('puestos_listar')

class puestosEliminar(generic.DeleteView):
    model = Puestos
    #form_class = PuestoForm
    template_name = 'puestos/eliminar.html' 
    success_url = reverse_lazy('puestos_listar')

'''