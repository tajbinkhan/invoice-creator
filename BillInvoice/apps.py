from django.apps import AppConfig


class BillinvoiceConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'BillInvoice'

	def ready(self):
		import BillInvoice.signals
