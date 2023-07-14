from django import forms
from .models import Clients
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
	class Meta:
		model = Clients
		fields = '__all__'
		exclude = ('client_id',)
		widgets = {
			"client_name": forms.TextInput(attrs={
				'placeholder': 'Enter Your Client Name',
				'autocomplete': 'off'
			}),
			"office_address": forms.Textarea(attrs={
				'placeholder': 'Enter Your Client Office Address',
				'rows': '3',
			}),
		}

	def clean_client_name(self):
		client_name = self.cleaned_data['client_name']
		if self.instance.id is None:
			if Clients.objects.filter(client_name=client_name).exists():
				raise ValidationError("Client name exists. You can't add same client. But you can update them from client list.", 'client_name')
		return client_name