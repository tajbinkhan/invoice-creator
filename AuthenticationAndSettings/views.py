from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from allauth.account.views import LoginView
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, SettingsForm
from .models import CustomUser, Settings
from core.decorators import superuser_required

# Create your views here.
@login_required
def profile(request):
	template_name = "profile/index.html"
	user = get_object_or_404(CustomUser, pk=request.user.id)
	form = CustomUserForm(request.POST or None, instance=user)
	if request.method == "POST":
		form = CustomUserForm(request.POST or None, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, "Profile updated successfully!")
			return redirect("profile")
	context = {"form": form}
	return render(request, template_name, context)


@login_required
def delete_account(request):
	if request.method == "POST":
		user = request.user
		if not user.is_superuser:
			user.delete()
			return JsonResponse({"success": True})
	return JsonResponse({"success": False})


class CustomLoginView(LoginView):
	def form_invalid(self, form):
		login = self.request.POST.get("login")
		password = self.request.POST.get("password")
		user = CustomUser.objects.filter(Q(username=login) | Q(email=login))
		if user:
			has_user = authenticate(self.request, username=login, password=password)

			if has_user is not None:
				if has_user.is_active:
					login(self.request, has_user)
					return redirect("dashboard")
				else:
					messages.error(self.request, "This account is inactive.")
			else:
				messages.error(self.request, "Incorrect password.")
		else:
			messages.error(self.request, "Account does not exist.")

		return self.render_to_response(self.get_context_data(form=form))


@superuser_required
def settings(request):
	template_name = "settings/index.html"
	settings = Settings.objects.last()
	if not settings:
		return redirect("add_settings")
	return render(request, template_name)


@superuser_required
def add_settings(request):
	template_name = "settings/form.html"
	settings = Settings.objects.last()
	if settings:
		return redirect("update_settings")
	else:
		form = SettingsForm()
		if request.method == "POST":
			form = SettingsForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				messages.success(request, "Settings added successfully!")
				return redirect("settings")
		context = {"form": form, "head_title": "Add Settings", "button_name": "Add"}
	return render(request, template_name, context)


@superuser_required
def update_settings(request):
	template_name = "settings/form.html"
	settings = Settings.objects.last()
	if settings:
		form = SettingsForm(instance=settings)
		if request.method == "POST":
			form = SettingsForm(request.POST, request.FILES, instance=settings)
			if form.is_valid():
				form.save()
				messages.success(request, "Settings updated successfully!")
				return redirect("settings")
		context = {
			"form": form,
			"head_title": "Update Settings",
			"button_name": "Update",
		}
		return render(request, template_name, context)
	else:
		return redirect("add_settings")


def terms_conditions(request):
	template_name = "method-pages/terms-and-conditions.html"
	return render(request, template_name)


def privacy_policy(request):
	template_name = "method-pages/privacy-policy.html"
	return render(request, template_name)
