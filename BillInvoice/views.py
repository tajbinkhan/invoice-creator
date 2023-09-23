import math
import locale
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from .models import BillInvoice, BillInvoiceGoods
from .forms import BillInvoiceForm, BillInvoiceGoodsFormSet
from Preferences.models import Preferences, Description
from django.contrib import messages
from num2words import num2words
from django.http import JsonResponse
from core.decorators import superuser_required

# Create your views here.
@superuser_required
def index(request):
	template_name = "bill/index.html"
	return render(request, template_name)


@superuser_required
def list_bill_invoice_api(request):
	invoice_list = BillInvoice.objects.all().prefetch_related(
		Prefetch("bill_goods", queryset=BillInvoiceGoods.objects.all().order_by("id"))
	)

	invoice_data = []

	for invoice in invoice_list:
		locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
		date = invoice.created_at.strftime("%b %d, %Y")
		created_at = invoice.created_at.strftime("%b %d, %Y")

		goods_data = []
		for goods in invoice.bill_goods.all():
			goods_data.append(
				{
					"color": goods.color,
					"count": goods.count,
					"quantity": goods.quantity,
					"unit": goods.unit,
					"unit_price": goods.unit_price,
				}
			)

		try:
			invoice_data.append(
				{
					"invoice_id": invoice.invoice_id,
					"invoice_number": invoice.invoice_number,
					"client": invoice.client.client_name,
					"goods_data": goods_data,
					"currency": invoice.currency,
					"custom_total_amount": invoice.custom_total_amount,
					"calculate_total_goods_value": invoice.calculate_total_goods_value(),
					"date": date,
					"created_at": created_at,
				}
			)
		except:
			invoice_data.append(
				{
					"invoice_id": invoice.invoice_id,
					"invoice_number": invoice.invoice_number,
					"client": "No Client",
					"goods_data": goods_data,
					"currency": invoice.currency,
					"custom_total_amount": invoice.custom_total_amount,
					"calculate_total_goods_value": invoice.calculate_total_goods_value(),
					"date": date,
					"created_at": created_at,
				}
			)

	response = {
		"invoice_data": invoice_data,
	}
	return JsonResponse(response)


@superuser_required
def add_invoice(request):
	template_name = "bill/form.html"
	if request.method == "POST":
		form = BillInvoiceForm(request.POST)
		formset = BillInvoiceGoodsFormSet(request.POST)
		if form.is_valid() and formset.is_valid():
			invoice = form.save()
			formset.instance = invoice
			formset.save()
			messages.success(request, "Invoice created successfully!")
			return redirect("bill_invoice")
	else:
		form = BillInvoiceForm()
		formset = BillInvoiceGoodsFormSet()
	context = {
		"form": form,
		"formset": formset,
		"head_title": "Bill Invoice Form",
		"button_name": "Add Invoice",
	}
	return render(request, template_name, context)


@superuser_required
def detail_invoice(request, invoice_id):
	template_name = "bill/details.html"
	preferences = Preferences.objects.last()
	bill_invoice = BillInvoice.objects.prefetch_related("bill_goods").get(
		invoice_id=invoice_id
	)
	description = Description.objects.last()

	number2words = None
	if bill_invoice.custom_total_amount:
		number_str = str(bill_invoice.custom_total_amount)
		number = float(number_str.replace(",", ""))
		integer_words = (
			num2words(math.floor(number), lang="en_IN")
			.replace(",", "")
			.replace(" and ", " ")
			.replace("lakh", "lac")
		)
		integer_part, decimal_part = number_str.split(".")
		decimal_words = (
			num2words(decimal_part, lang="en_IN")
			.replace(",", "")
			.replace(" and ", " ")
			.replace("lakh", "lac")
		)
		if int(decimal_part) > 0:
			number2words = f"{integer_words} Point {decimal_words}"
		else:
			number2words = integer_words
	else:
		number_str = str(bill_invoice.calculate_total_goods_value())
		number = float(number_str.replace(",", ""))
		integer_words = (
			num2words(math.floor(number), lang="en_IN")
			.replace(",", "")
			.replace(" and ", " ")
			.replace("lakh", "lac")
		)
		decimal_part = round((number % 1) * 100)
		decimal_words = (
			num2words(decimal_part, lang="en_IN")
			.replace(",", "")
			.replace(" and ", " ")
			.replace("lakh", "lac")
		)
		if decimal_part > 0:
			number2words = f"{integer_words} Point {decimal_words}"
		else:
			number2words = integer_words

	context = {
		"bill_invoice": bill_invoice,
		"preferences": preferences,
		"number2words": number2words,
		"description": description,
	}
	return render(request, template_name, context)


@superuser_required
def update_invoice(request, invoice_id):
	template_name = "bill/form.html"
	bill_invoice_id = BillInvoice.objects.get(invoice_id=invoice_id)
	if request.method == "POST":
		form = BillInvoiceForm(request.POST, instance=bill_invoice_id)
		formset = BillInvoiceGoodsFormSet(request.POST, instance=bill_invoice_id)
		if form.is_valid() and formset.is_valid():
			invoice = form.save()
			formset.instance = invoice
			formset.save()
			messages.success(
				request, f"{bill_invoice_id.invoice_number} updated successfully!"
			)
			return redirect("bill_invoice")
	else:
		form = BillInvoiceForm(instance=bill_invoice_id)
		formset = BillInvoiceGoodsFormSet(instance=bill_invoice_id)
	context = {
		"form": form,
		"formset": formset,
		"head_title": "Bill Invoice Form",
		"button_name": "Update Invoice",
	}
	return render(request, template_name, context)


@superuser_required
def delete_invoice(request, invoice_id):
	bill_invoice_id = BillInvoice.objects.get(invoice_id=invoice_id)
	if request.method == "POST":
		bill_invoice_id.delete()
		messages.success(
			request, f"{bill_invoice_id.invoice_number} deleted successfully!"
		)
		return redirect("bill_invoice")

	return render(request, "base/delete_confirmation.html")
