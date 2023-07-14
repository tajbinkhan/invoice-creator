from django.contrib import admin
from .models import Clients

# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
	list_display = ('client_name', 'client_id', 'updated_at', 'created_at')
	search_fields = ['client_name', 'office_address']

admin.site.register(Clients, ClientsAdmin)