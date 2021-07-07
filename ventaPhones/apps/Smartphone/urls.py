
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from django.conf.urls.static import static
from .views import SmartphoneList

urlpatterns = [
    
    path('list_smartphones/', SmartphoneList.as_view(), name="list_alumnos"),
    
]