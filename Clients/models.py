from django.db import models

# Create your models here.

class Clients(models.Model):
	client_id = models.CharField(max_length=256, editable=False, blank=True, null=True)
	client_name = models.CharField(max_length=256)
	office_address = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Client'
		verbose_name_plural = 'Clients'

	def __str__(self):
		return self.client_name