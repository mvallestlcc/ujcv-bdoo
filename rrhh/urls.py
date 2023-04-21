
from django.urls import path
from . import views
from .views import *

urlpatterns = [
      # path('rrhh/expediente/index',views.expediente_index, name='expediente_index'),
      # path('rrhh/expediente/consulta',views.expediente_index2, name='expediente_index2'),
      # path('rrhh/expediente/nombres',views.expediente_index3, name='expediente_index3'),
       path('rrhh/departamentos/index',departamentoListar.as_view(), name='departamentos_listar'),
       path('rrhh/departamentos/agregar',departamentoAgregar.as_view(), name='departamentos_agregar'),
       path('rrhh/departamentos/editar/<int:pk>/',departamentosEditar.as_view(), name='departamentos_editar'),   
       path('rrhh/departamentos/eliminar/<int:pk>/',departamentosEliminar.as_view(), name='departamentos_eliminar'),        
  ]
