from django import forms
from django.contrib import admin
from django.db.models import Prefetch
from django.forms import BaseInlineFormSet, inlineformset_factory
from .models import BillInvoice, BillInvoiceGoods

# Register your models here.
class BillInvoiceGoodsChildFormSet(BaseInlineFormSet):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.extra = 0

class BillInvoiceGoodsInline(admin.TabularInline):
	model = BillInvoiceGoods
	formset = inlineformset_factory(
		BillInvoice,
		BillInvoiceGoods,
		formset=BillInvoiceGoodsChildFormSet,
		fields='__all__',
		extra=0,
		can_delete=True
	)

class BillInvoiceAdmin(admin.ModelAdmin):
	inlines = [BillInvoiceGoodsInline]
	list_display = ('__str__', 'get_products', 'date', 'updated_at', 'created_at')
	save_on_top = True
	search_fields = ['title', 'bill_number']

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		prefetch_goods = Prefetch('bill_goods', queryset=BillInvoiceGoods.objects.all().order_by('pk'))
		qs = qs.prefetch_related(prefetch_goods)
		return qs

	def get_products(self, obj):
		goods = obj.bill_goods.all()
		products = [f"{good.color} ({good.quantity} {good.unit} x {good.unit_price})" for good in goods]
		return ' | '.join(products) if products else ''

	get_products.short_description = 'Products'

admin.site.register(BillInvoice, BillInvoiceAdmin)
