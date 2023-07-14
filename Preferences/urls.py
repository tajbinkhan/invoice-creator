from django.urls import path
from . import views

urlpatterns = [
	path('', views.preferences, name='preferences'),
	path('add/', views.add_preferences, name='add_preferences'),
	path('update/', views.update_preferences, name='update_preferences'),
	path('description/', views.description, name='description'),
	path('description/add/', views.add_description, name='add_description'),
	path('description/update/', views.update_description, name='update_description'),
]
