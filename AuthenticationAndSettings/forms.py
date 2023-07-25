from django import forms
from .models import CustomUser, Settings
from allauth.account.forms import LoginForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomLoginForm(LoginForm):
	def __init__(self, *args, **kwargs):
		super(CustomLoginForm, self).__init__(*args, **kwargs)
		self.fields["login"].widget.attrs.update(
			{"placeholder": "Username or E-mail", "class": "textinput form-control"}
		)
		self.fields["remember"].widget.attrs.update(
			{"checked": "true", "class": "form-check-input", "id": "remember-check"}
		)


class CustomUserForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserForm, self).__init__(*args, **kwargs)
		self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
		self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"

	class Meta:
		model = CustomUser
		fields = ["first_name", "last_name", "profile_picture"]


class SettingsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SettingsForm, self).__init__(*args, **kwargs)
		self.fields["terms_conditions"].widget.attrs[
			"placeholder"
		] = "Website Terms & Conditions..."
		self.fields["privacy_policy"].widget.attrs[
			"placeholder"
		] = "Website Privacy Policy..."
		self.fields["terms_conditions"].label = "Website Terms & Conditions"
		self.fields["privacy_policy"].label = "Website Privacy Policy"

	class Meta:
		model = Settings
		fields = "__all__"
