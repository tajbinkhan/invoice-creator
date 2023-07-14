from django import forms
from datetime import datetime
from django.conf import settings
from .models import BillInvoice, BillInvoiceGoods, CURRENCY, UNIT

class BillInvoiceForm(forms.ModelForm):
	class Meta:
		model = BillInvoice
		fields = '__all__'
		exclude = ('invoice_id',)
		help_texts = {
			'custom_total_amount': '<i>Leave it empty if you want to generate automatically.</i>',
		}
		widgets = {
			'invoice_number': forms.TextInput(attrs={
				'placeholder': 'Enter invoice number'
			}),
			'description': forms.TextInput(attrs={
				'placeholder': 'Enter product description'
			}),
			'date': forms.DateInput(attrs={
				'type': 'text',
				'placeholder': 'Pick up a date',
				'class': 'form-control date-picker',
				'data-date-format': 'dd/mm/yyyy',
				'autocomplete': 'off',
				'readonly': 'on'
			}),
			'currency': forms.Select(attrs={
				'class': 'currencypicker',
				'data-placeholder': 'Select a currency'
			}),
			'client': forms.Select(attrs={
				'class': 'clientpicker',
				'data-placeholder': 'Select a client'
			}),
			'custom_total_amount': forms.TextInput(attrs={
				'placeholder': 'Enter custom total amount (Leave it empty if you want to generate automatically.)'
			})
		}

class BillInvoiceGoodsForm(forms.ModelForm):
	class Meta:
		model = BillInvoiceGoods
		fields = '__all__'
		exclude = ('id',)
		widgets = {
			'color': forms.TextInput(attrs={
				'placeholder': 'Enter color name'
			}),
			'count': forms.TextInput(attrs={
				'placeholder': 'Enter color count'
			}),
			'quantity': forms.TextInput(attrs={
				'placeholder': 'Enter product quantity'
			}),
			'unit_price': forms.TextInput(attrs={
				'placeholder': 'Enter product unit price'
			}),
			'unit': forms.Select(attrs={
				'class': 'unitpicker',
				'data-placeholder': 'Select a unit'
			})
		}

BillInvoiceGoodsFormSet = forms.inlineformset_factory(
	BillInvoice,
	BillInvoiceGoods,
	form=BillInvoiceGoodsForm,
	extra=0,
	can_delete=True
)