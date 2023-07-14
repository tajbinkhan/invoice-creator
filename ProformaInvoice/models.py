from django.db import models
from Clients.models import Clients
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
number_validator = RegexValidator(
	r'^\d*\.?\d*$',
	'Enter a valid number.',
	'invalid'
)

UNIT = [
	('KG', 'KG'),
	('LBS', 'LBS'),
]

CURRENCY = [
	('BDT', 'BDT'),
	('USD', 'USD'),
]

class ProformaInvoice(models.Model):
	invoice_id = models.CharField(max_length=256, editable=False, blank=True, null=True)
	invoice_number = models.CharField(max_length=256)
	date = models.DateField()
	client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
	currency = models.CharField(choices=CURRENCY, max_length=256)
	custom_total_amount = models.CharField(max_length=256, validators=[number_validator], blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Proforma Invoice'
		verbose_name_plural = 'Proforma Invoices'

	def calculate_total_goods_value(self):
		total_value = 0
		for goods in self.proforma_goods.all():
			total_value += goods.calculate_total_value()
		return total_value

	def __str__(self):
		return self.invoice_number

class ProformaInvoiceGoods(models.Model):
	proforma_invoice = models.ForeignKey(ProformaInvoice, on_delete=models.CASCADE, related_name='proforma_goods')
	product = models.CharField(max_length=256)
	quantity = models.CharField(max_length=256, validators=[number_validator])
	unit = models.CharField(choices=UNIT, max_length=256)
	unit_price = models.CharField(max_length=256, validators=[number_validator])

	class Meta:
		verbose_name_plural = 'Goods'

	def calculate_total_value(self):
		try:
			quantity = float(self.quantity)
			unit_price = float(self.unit_price)
			return quantity * unit_price
		except ValueError:
			raise ValidationError("Invalid quantity or unit price.")

	def __str__(self):
		return f"{self.product} {self.quantity}{self.unit}, Price - {self.unit_price}{self.proforma_invoice.currency}"