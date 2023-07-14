import os
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def logo(instance, filename):
	new_filename = 'logo'
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f'site-images/{final_filename}'

def signature(instance, filename):
	new_filename = 'signature'
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f'site-images/{final_filename}'

def watermark(instance, filename):
	new_filename = 'watermark'
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f'site-images/{final_filename}'

class Description(models.Model):
	beneficiary = models.TextField()
	terms_conditions = RichTextField(verbose_name='Terms and Conditions')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.beneficiary

class Preferences(models.Model):
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256)
	address = models.CharField(max_length=256)
	contact = models.CharField(max_length=256)
	email_address = models.EmailField(max_length=256)
	logo = models.ImageField(upload_to=logo)
	signature = models.ImageField(upload_to=signature)
	watermark = models.ImageField(upload_to=watermark)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Preference'
		verbose_name_plural = 'Preferences'

	def __str__(self):
		return self.title
