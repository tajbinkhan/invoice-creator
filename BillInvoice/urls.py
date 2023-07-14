from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='bill_invoice'),
	path('list/api/', views.list_bill_invoice_api, name='list_bill_invoice_api'),
	path('add/', views.add_invoice, name='add_bill_invoice'),
	path('update/<str:invoice_id>/', views.update_invoice, name='update_bill_invoice'),
	path('delete/<str:invoice_id>/', views.delete_invoice, name='delete_bill_invoice'),
	path('<str:invoice_id>/', views.detail_invoice, name='detail_bill_invoice'),
]