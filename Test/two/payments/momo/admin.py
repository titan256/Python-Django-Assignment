from django.contrib import admin

from .models import Customer,MomoRequest

@admin.register(MomoRequest)
class MoMoRequestAdmin(admin.ModelAdmin):

	list_display = ('customername', 'mobile', 'amount', 'transref','status')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

	list_display = ('CustomerName','CustomerId','CustomerTel')

