from django.urls import path,include
from .views import abc,pqr

urlpatterns = [
  path('dd',abc),
  path('home',pqr),
  path('admin/',include('adminp.urls'))
]
