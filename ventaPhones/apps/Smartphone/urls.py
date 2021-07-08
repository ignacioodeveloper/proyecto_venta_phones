
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from django.conf.urls.static import static
from .views import SmartphoneList, SmartphoneListCliente, SmartphoneUpdate, SmartphoneDelete

from rest_framework.urlpatterns import format_suffix_patterns
from apps.Smartphone import views


urlpatterns = [
    
    path('list/', SmartphoneList.as_view(), name="list_smartphones"),
    path('editar/<int:pk>', SmartphoneUpdate.as_view(), name="update_smartphone"),
    path('eliminar/<int:pk>', SmartphoneDelete.as_view(), name="delete_smartphone"),
    path('list_cliente', SmartphoneListCliente.as_view(), name="list_cliente_smartphone")
]


urlpatterns += [
    
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>', views.API_objects_details.as_view()),   
    
]

urlpattenrs = format_suffix_patterns(urlpatterns)