from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserver_summary, name="reserver_summary"),
    path('add/', views.reserver_add, name="reserver_add"),
    path('delete/', views.reserver_delete, name="reserver_delete"),
    path('update/', views.reserver_update, name="reserver_update"),
]
