import locale
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.defaultfilters import truncatewords
from django.contrib import messages
from .models import Clients
from .forms import ClientForm
from core.decorators import superuser_required

# Create your views here.
# ------------- Client Section Start -------------#
@superuser_required
def clients(request):
	template_name = "clients/index.html"
	clients = Clients.objects.all()
	context = {"clients": clients}
	return render(request, template_name, context)


@superuser_required
def clients_api(request):
	clients = Clients.objects.all()

	data = []
	for client in clients:
		locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
		updated_at = client.updated_at.strftime("%b %d, %Y")
		created_at = client.created_at.strftime("%b %d, %Y")

		data.append(
			{
				"client_id": client.client_id,
				"client_name": client.client_name,
				"office_address": truncatewords(client.office_address, 3),
				"updated_at": updated_at,
				"created_at": created_at,
			}
		)

	response = {
		"data": data,
	}
	return JsonResponse(response)


@superuser_required
def client_name_api(request):
	search_term = request.GET.get("q", "")
	clients = Clients.objects.filter(client_name__icontains=search_term).values(
		"id", "client_name"
	)
	return JsonResponse(list(clients), safe=False)


@superuser_required
def add_client(request):
	template_name = "clients/form.html"
	if request.method == "POST":
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Client added successfully!")
			return redirect("clients")
		else:
			messages.error(request, "Client added failed!")
	else:
		form = ClientForm()
	context = {
		"form": form,
		"head_title": "Add New Client",
		"button_name": "Add Client",
	}
	return render(request, template_name, context)


@superuser_required
def update_client(request, client_id):
	template_name = "clients/form.html"
	client = get_object_or_404(Clients, client_id=client_id)
	form = ClientForm(request.POST or None, instance=client)
	if request.method == "POST":
		form = ClientForm(request.POST, instance=client)
		if form.is_valid():
			form.save()
			messages.success(request, f"{client.client_name} updated successfully!")
			return redirect("clients")
		else:
			messages.error(request, "Client updated failed!")
	context = {
		"form": form,
		"head_title": "Update Client",
		"button_name": "Update Client",
	}
	return render(request, template_name, context)


@superuser_required
def delete_client(request, client_id):
	if request.method == "POST":
		client = get_object_or_404(Clients, client_id=client_id)
		client.delete()
		messages.success(request, f"{client.client_name} deleted successfully!")
		return redirect("clients")
	else:
		messages.error(request, "Client deleted failed!")
		return redirect("clients")


# ------------- Client Section End -------------#
