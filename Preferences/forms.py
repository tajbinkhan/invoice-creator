from django import forms
from .models import Description, Preferences

class DescriptionForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DescriptionForm, self).__init__(*args, **kwargs)
		self.fields['beneficiary'].widget.attrs['placeholder'] = 'Beneficiary Details...'
		self.fields['beneficiary'].widget.attrs['rows'] = '3'
		self.fields['beneficiary'].label = 'Beneficiary Details'

		self.fields['terms_conditions'].widget.attrs['placeholder'] = 'Terms & Conditions...'
		self.fields['terms_conditions'].label = 'Terms & Conditions'

	class Meta:
		model = Description
		fields = '__all__'

class PreferencesForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PreferencesForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs['placeholder'] = 'Company Name...'
		self.fields['title'].label = 'Company Name'

		self.fields['subtitle'].widget.attrs['placeholder'] = 'Company Tagline...'
		self.fields['subtitle'].label = 'Company Tagline'

		self.fields['address'].widget.attrs['placeholder'] = 'Company Address...'
		self.fields['address'].label = 'Company Address'

		self.fields['contact'].widget.attrs['placeholder'] = 'Company Phone Number...'
		self.fields['contact'].label = 'Company Phone Number'

		self.fields['email_address'].widget.attrs['placeholder'] = 'Company Email Address...'
		self.fields['email_address'].label = 'Company Email Address'

		self.fields['logo'].label = 'Company Logo'
		self.fields['signature'].label = 'Owner Signature'
		self.fields['watermark'].label = 'Watermark'

	class Meta:
		model = Preferences
		fields = '__all__'
