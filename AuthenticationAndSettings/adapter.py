from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
from django import forms


class CustomAccountAdapter(DefaultAccountAdapter):
	def save_user(self, request, user, form, commit=True):
		user = super().save_user(request, user, form, commit=False)
		user.is_active = True
		if commit:
				user.save()
		return user

	def clean_email(self, email):
		email = super().clean_email(email)
		UserModel = get_user_model()
		if UserModel.objects.filter(email=email).exists():
			raise forms.ValidationError("This e-mail address is already associated with another account.")
		return email