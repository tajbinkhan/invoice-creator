from django.shortcuts import render
from core.decorators import superuser_required
from ProformaInvoice.models import ProformaInvoice
from BillInvoice.models import BillInvoice
from Clients.models import Clients

# Create your views here.
@superuser_required
def index(request):
	template_name = 'dashboard/index.html'
	proforma_invoice = ProformaInvoice.objects.all().count()
	bill_invoice = BillInvoice.objects.all().count()
	clients = Clients.objects.all().count()

	latest_proforma_invoice = ProformaInvoice.objects.last()
	latest_bill_invoice = BillInvoice.objects.last()

	context = {
		'proforma_invoice': proforma_invoice,
		'bill_invoice': bill_invoice,
		'clients': clients,
		'latest_proforma_invoice': latest_proforma_invoice,
		'latest_bill_invoice': latest_bill_invoice,
	}
	return render(request, template_name, context)