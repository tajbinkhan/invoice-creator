from django.contrib import admin
from .models import Description, Preferences

# Register your models here.
class DescriptionAdmin(admin.ModelAdmin):
	list_display = ('beneficiary', 'updated_at', 'created_at')

class PreferencesAdmin(admin.ModelAdmin):
	list_display = ('title', 'subtitle', 'email_address', 'address', 'contact')
	search_fields = ['title', 'subtitle', 'email_address']

admin.site.register(Description, DescriptionAdmin)
admin.site.register(Preferences, PreferencesAdmin)