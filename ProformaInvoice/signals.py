import hashlib
from .models import ProformaInvoice, ProformaInvoiceGoods
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=ProformaInvoice)
def generate_proforma_invoice_id(sender, instance, created, **kwargs):
	if created or not instance.invoice_id:
		post_id_str = str(instance.id).encode()
		hash_object = hashlib.sha256(post_id_str)
		instance.invoice_id = hash_object.hexdigest()
		instance.save()