from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse

def superuser_required(view_func):
	template_name = 'method-pages/405.html'
	def check_superuser(user):
		if user.is_superuser:
				return True
		else:
				return False

	def decorator(request, *args, **kwargs):
		next_path = request.path
		if not request.user.is_authenticated:
			return redirect(f"{reverse('account_login')}?next={next_path}")
		if not check_superuser(request.user):
			return render(request, template_name)
		return view_func(request, *args, **kwargs)

	return decorator