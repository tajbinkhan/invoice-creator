from django.apps import AppConfig


class ProformainvoiceConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'ProformaInvoice'

	def ready(self):
		import ProformaInvoice.signals
