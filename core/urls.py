from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AuthenticationAndSettings.views import CustomLoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/', RedirectView.as_view(url=reverse_lazy('account_login'), permanent=False)),
	path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
	path('accounts/', include('allauth.urls')),
	path('', include('Dashboard.urls')),
	path('proforma-invoice/', include('ProformaInvoice.urls')),
	path('bill-invoice/', include('BillInvoice.urls')),
	path('clients/', include('Clients.urls')),
	path('preferences/', include('Preferences.urls')),
	path('', include('AuthenticationAndSettings.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
