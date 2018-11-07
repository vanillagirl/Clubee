from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('clubs', views.lista, name='lista'),
    path('club/<int:pk>/', views.clubdetalle, name='clubdetalle'),
]
