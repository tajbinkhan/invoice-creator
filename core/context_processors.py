from django.urls import reverse
from Preferences.models import Preferences
from AuthenticationAndSettings.models import Settings

def breadcrumbs(request):
	breadcrumbs = []
	path_parts = request.path.split('/')[1:]
	if path_parts[0] == '""':
		return {breadcrumbs:'Dashboard'}
	else:
		for i, part in enumerate(path_parts):
			if part:
				url = '/'.join(path_parts[:i+1])
				name = part.capitalize()
				breadcrumbs.append({'name': name, 'url': url})

	return {'breadcrumbs': breadcrumbs}

def global_context(request):
	global_preferences = Preferences.objects.last()
	profile_picture = None
	full_name = None
	if request.user.is_authenticated:
		full_name = request.user.get_full_name()
		profile_picture = request.user.profile_picture

	global_settings = Settings.objects.last()
	context = {
		'global_preferences': global_preferences,
		'global_settings': global_settings,
		'site_name': 'Tajmoho International',
		'profile_picture': profile_picture,
		'full_name': full_name,
	}
	return context

