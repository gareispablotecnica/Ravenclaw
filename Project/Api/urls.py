from django.urls import path
# --> Importamos las Vistas
from .views import *

urlpatterns = [
    # ---> ulr, metodo, html
    path('', Home, name='home'),
    path('Productos/', Productos, name='Productos'),
    path('NuevoProducto/', NuevoProductos, name='nuevo_producto'),
    path('ModificarProductos/<Codigo>', ModificarProductos, name='Modificar'),
]
