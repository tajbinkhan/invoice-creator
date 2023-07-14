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

class BillInvoice(models.Model):
	invoice_id = models.CharField(max_length=256, editable=False, blank=True, null=True)
	invoice_number = models.CharField(max_length=256)
	description = models.CharField(max_length=256)
	date = models.DateField()
	client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True)
	currency = models.CharField(choices=CURRENCY, max_length=256)
	custom_total_amount = models.CharField(max_length=256, validators=[number_validator], blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Bill Invoice'
		verbose_name_plural = 'Bill Invoices'

	def calculate_total_goods_value(self):
		total_value = 0
		for goods in self.bill_goods.all():
			total_value += goods.calculate_total_value()
		return total_value

	def __str__(self):
		return self.invoice_number

class BillInvoiceGoods(models.Model):
	bill_invoice = models.ForeignKey(BillInvoice, on_delete=models.CASCADE, related_name='bill_goods')
	color = models.CharField(max_length=256)
	count = models.CharField(max_length=256, blank=True, null=True)
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
		return f"{self.color} {self.quantity}{self.unit}, Price - {self.unit_price}{self.bill_invoice.currency}"