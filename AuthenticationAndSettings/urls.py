from django.urls import path
from . import views

urlpatterns = [
	path('accounts/profile/', views.profile, name='profile'),
	path('accounts/delete/', views.delete_account, name='delete_account'),
	path('settings/', views.settings, name='settings'),
	path('settings/add/', views.add_settings, name='add_settings'),
	path('settings/update/', views.update_settings, name='update_settings'),
	path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
	path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]