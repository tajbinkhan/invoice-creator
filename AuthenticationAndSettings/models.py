import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from core.utils import optimize_image

# Create your models here.
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext


def profile_picture(instance, filename):
	new_filename = instance.username
	name, ext = get_filename_ext(filename)
	final_filename = f"{new_filename}{ext}"
	return f"profile-picture/{final_filename}"


def website_logo(instance, filename):
	new_filename = "website-logo"
	name, ext = get_filename_ext(filename)
	final_filename = f"{new_filename}{ext}"
	return f"website/{final_filename}"


def mobile_logo(instance, filename):
	new_filename = "mobile-logo"
	name, ext = get_filename_ext(filename)
	final_filename = f"{new_filename}{ext}"
	return f"website/{final_filename}"


class CustomUser(AbstractUser):
	profile_picture = models.ImageField(
		upload_to=profile_picture, blank=True, null=True
	)

	def save(self, *args, **kwargs):
		try:
			self.profile_picture = optimize_image(self.profile_picture, 100, 100)
		except FileNotFoundError as e:
			print(e)
		super().save(*args, **kwargs)


class Settings(models.Model):
	terms_conditions = RichTextField(verbose_name="Website Terms and Conditions")
	privacy_policy = RichTextField(verbose_name="Website Privacy Policy")
	website_logo = models.ImageField(upload_to=website_logo, blank=True, null=True)
	mobile_logo = models.ImageField(upload_to=mobile_logo, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Settings"

	def save(self, *args, **kwargs):
		try:
			self.website_logo = optimize_image(self.website_logo, 167, 167)
			self.mobile_logo = optimize_image(self.mobile_logo, 23, 22)
		except FileNotFoundError as e:
			print(e)
		super().save(*args, **kwargs)

	def __str__(self):
		return "Website Staff"
