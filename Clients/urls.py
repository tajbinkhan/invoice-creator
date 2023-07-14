from django.urls import path
from . import views

urlpatterns = [
	path('', views.clients, name="clients"),
	path('api/', views.clients_api, name="clients_api"),
	path('api/name/', views.client_name_api, name="client_name_api"),
	path('add/', views.add_client, name="add_client"),
	path('update/<str:client_id>/', views.update_client, name="update_client"),
	path('delete/<str:client_id>/', views.delete_client, name="delete_client"),
]
