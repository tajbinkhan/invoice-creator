from django.db.models.signals import post_init, pre_save
from django.dispatch import receiver
from core.utils import optimize_image
from .models import Settings, CustomUser

@receiver(pre_save, sender=Settings)
def replace_images(sender, instance, **kwargs):
	if instance.pk:
		try:
			prev_instance = Settings.objects.get(pk=instance.pk)
		except Settings.DoesNotExist:
			prev_instance = None

		if prev_instance:
			try:
				if prev_instance.website_logo != instance.website_logo:
					prev_instance.website_logo.storage.delete(prev_instance.website_logo.path)
				if prev_instance.mobile_logo != instance.mobile_logo:
					prev_instance.mobile_logo.storage.delete(prev_instance.mobile_logo.path)
			except ValueError as e:
				print(e)

@receiver(pre_save, sender=CustomUser)
def replace_profile_image(sender, instance, **kwargs):
	if instance.pk:
		try:
			prev_instance = CustomUser.objects.get(pk=instance.pk)
		except CustomUser.DoesNotExist:
			prev_instance = None

		if prev_instance:
			try:
				if prev_instance.profile_picture != instance.profile_picture:
					prev_instance.profile_picture.storage.delete(prev_instance.profile_picture.path)
			except ValueError as e:
				print(e)
