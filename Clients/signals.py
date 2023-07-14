import hashlib
from .models import Clients
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Clients)
def generate_client_id(sender, instance, created, **kwargs):
	if created or not instance.client_id:
		post_id_str = str(instance.id).encode()
		hash_object = hashlib.sha256(post_id_str)
		instance.client_id = hash_object.hexdigest()
		instance.save()
