
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from django.conf.urls.static import static
from .views import SmartphoneList, SmartphoneListCliente, SmartphoneUpdate, SmartphoneDelete

urlpatterns = [
    
    path('list/', SmartphoneList.as_view(), name="list_smartphones"),
    path('editar/<int:pk>', SmartphoneUpdate.as_view(), name="update_smartphone"),
    path('eliminar/<int:pk>', SmartphoneDelete.as_view(), name="delete_smartphone"),
    path('list_cliente', SmartphoneListCliente.as_view(), name="list_cliente_smartphone")
]