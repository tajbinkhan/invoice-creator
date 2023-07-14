from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import CustomUser, Settings

class CustomUserAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)

	list_display = ('username', 'email', 'get_full_name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
	save_on_top = True

	def get_full_name(self, obj):
		return obj.get_full_name()

	get_full_name.short_description = 'Full Name'

class SettingsAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'updated_at', 'created_at']
	save_on_top = True

admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Settings, SettingsAdmin)
