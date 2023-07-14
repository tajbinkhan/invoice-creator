from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='proforma_invoice'),
	path('list/api/', views.list_proforma_invoice_api, name='list_proforma_invoice_api'),
	path('add/', views.add_invoice, name='add_proforma_invoice'),
	path('update/<str:invoice_id>/', views.update_invoice, name='update_proforma_invoice'),
	path('delete/<str:invoice_id>/', views.delete_invoice, name='delete_proforma_invoice'),
	path('<str:invoice_id>/', views.detail_invoice, name='detail_proforma_invoice'),
]