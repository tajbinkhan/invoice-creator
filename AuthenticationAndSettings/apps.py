from django.apps import AppConfig


class AuthenticationandsettingsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'AuthenticationAndSettings'
	verbose_name = 'Authentication & Settings'

	def ready(self):
		import AuthenticationAndSettings.signals
