from django.urls import path
from .views import *

urlpatterns = [
  path('',index,name='ahome'),
  path('form',form,name="raam"),
  path('about',about,name='adminabout')
]
