from django.urls import path,include
from . import views
urlpatterns = [
    path('base/',views.Base, name='base'),
    path('result/',views.Result, name='result'),
    path('',views.home, name='home'),
    path('team',views.Team, name='team'),
 
    
]
