from django.shortcuts import render, redirect
from .models import Description, Preferences
from .forms import DescriptionForm, PreferencesForm
from core.decorators import superuser_required

# Create your views here.

#------------- Preferences Section Start -------------#
@superuser_required
def preferences(request):
	template_name = 'preferences/index.html'
	preferences = Preferences.objects.last()
	if not preferences:
		return redirect('add_preferences')
	context = {
		'preferences': preferences
	}
	return render(request, template_name, context)

@superuser_required
def add_preferences(request):
	template_name = 'preferences/form.html'
	preferences = Preferences.objects.last()
	if preferences:
		return redirect('update_preferences')
	else:
		form = PreferencesForm()
		if request.method == 'POST':
			form = PreferencesForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('preferences')
		context = {
			'form': form,
			'head_title': 'Add Preferences',
			'button_name': 'Add'
		}
	return render(request, template_name, context)

@superuser_required
def update_preferences(request):
	template_name = 'preferences/form.html'
	preferences = Preferences.objects.last()
	if preferences:
		form = PreferencesForm(instance=preferences)
		if request.method == 'POST':
			form = PreferencesForm(request.POST, request.FILES, instance=preferences)
			if form.is_valid():
				form.save()
				return redirect('preferences')
		context = {
			'form': form,
			'head_title': 'Update Preferences',
			'button_name': 'Update'
		}
		return render(request, template_name, context)
	else:
		return redirect('add_preferences')

#------------- Preferences Section End -------------#

#------------- Description Section Start -------------#
@superuser_required
def description(request):
	template_name = 'description/index.html'
	description = Description.objects.last()
	if not description:
		return redirect('add_description')
	context = {
		'description': description
	}
	return render(request, template_name, context)

@superuser_required
def add_description(request):
	template_name = 'description/form.html'
	description = Description.objects.last()
	if description:
		return redirect('update_description')
	else:
		form = DescriptionForm()
		if request.method == 'POST':
			form = DescriptionForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('description')
		context = {
			'form': form,
			'head_title': 'Add Description',
			'button_name': 'Add'
		}
		return render(request, template_name, context)

@superuser_required
def update_description(request):
	template_name = 'description/form.html'
	description = Description.objects.last()
	if description:
		form = DescriptionForm(instance=description)
		if request.method == 'POST':
			form = DescriptionForm(request.POST, instance=description)
			if form.is_valid():
				form.save()
				return redirect('description')
		context = {
			'form': form,
			'head_title': 'Update Description',
			'button_name': 'Update'
		}
		return render(request, template_name, context)
	else:
		return redirect('add_description')

#------------- Description Section End -------------#