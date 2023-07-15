from django import forms
from datetime import datetime
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import ProformaInvoice, ProformaInvoiceGoods, CURRENCY, UNIT

class ProformaInvoiceForm(forms.ModelForm):
	class Meta:
		model = ProformaInvoice
		fields = '__all__'
		exclude = ('invoice_id',)
		help_texts = {
			'custom_total_amount': '<i>Leave it empty if you want to generate automatically.</i>',
			'client': '<i>You can add clients from <a href="/clients/add/" target="_blank">here</a>.</i>',
		}
		widgets = {
			'invoice_number': forms.TextInput(attrs={
				'placeholder': 'Enter invoice number'
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

class ProformaInvoiceGoodsForm(forms.ModelForm):
	class Meta:
		model = ProformaInvoiceGoods
		fields = '__all__'
		exclude = ('id',)
		widgets = {
			'product': forms.TextInput(attrs={
				'placeholder': 'Enter product name'
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

ProformaInvoiceGoodsFormSet = forms.inlineformset_factory(
	ProformaInvoice,
	ProformaInvoiceGoods,
	form=ProformaInvoiceGoodsForm,
	extra=0,
	can_delete=True
)