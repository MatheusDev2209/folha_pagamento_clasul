from django.urls import path
from  funcionarios import views

urlpatterns = [
    path('funcionarios/', views.funcionario),
    #path('recipes/<int:id>/', views.recipes),
    ] 