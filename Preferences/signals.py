from django.db.models.signals import post_init, pre_save
from django.dispatch import receiver
from core.utils import optimize_image
from .models import Preferences

@receiver(pre_save, sender=Preferences)
def replace_images(sender, instance, **kwargs):
	if instance.pk:
		try:
			prev_instance = Preferences.objects.get(pk=instance.pk)
		except Preferences.DoesNotExist:
			prev_instance = None

		if prev_instance:
			try:
				if prev_instance.logo != instance.logo:
					prev_instance.logo.storage.delete(prev_instance.logo.path)
				if prev_instance.signature != instance.signature:
					prev_instance.signature.storage.delete(prev_instance.signature.path)
				if prev_instance.watermark != instance.watermark:
					prev_instance.watermark.storage.delete(prev_instance.watermark.path)
			except ValueError as e:
				print(e)
