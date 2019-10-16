from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, timedelta
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import uuid
from .mtn import MtnMomo

class Customer(models.Model):
	"""Model representing a Fenix Registered Customer"""

	CustomerName = models.CharField(max_length=200, help_text='Insert Customer Name')
	CustomerId   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	CustomerTel  = PhoneNumberField(help_text='Enter Phone Number linked to Mobile Money +256--')
	Location 	 = models.CharField(max_length=200, help_text='Insert Customer Location',default='Kampala')

	def __str__(self):
		""" String Representing Customer Class """
		return f'{self.CustomerName}'

class MomoRequest(models.Model):

	"""Model representing an Mtn MoMo Payment request"""

	customername = models.ForeignKey('Customer',null=False,on_delete=models.CASCADE)
	mobile 	     = models.CharField(max_length=15, help_text='Insert Customer Mobile',default='')
	amount 		 = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	external_id  = models.CharField(max_length=15, help_text='Insert Customer Mobile (256****)',default='')
	payee_note   = models.CharField(max_length=200, help_text='Insert Payee Note',default='') 
	payer_message= models.CharField(max_length=200, help_text='Insert Payment Message',default='')
	currency 	 = models.CharField(max_length=3, help_text='EUR / UGX',default='EUR')
	reqtyp  	 = models.CharField(max_length=200, help_text='Insert Request Type',default='Collection')
	transref 	 = models.CharField(max_length=200, help_text='Transaction Reference from MTN',default='')
	financialTransactionId = models.CharField(max_length=200, help_text='Financial Transaction ID from MTN',default='')
	status       = models.CharField(max_length=200, help_text='Payment Status',default='Pending')

	def __str__(self):
		""" String Representing MoMo request Class """
		return f'{self.customername}'


#Defining the signals for class
@receiver(post_save, sender=MomoRequest)
def save_momorequest(sender,instance,created,**kwargs):

	"""This is a signal that is autommatically triggered on model MoMoRequest Save and it interacts with MTN MoMo API"""

	if not getattr(instance, 'processed', False):
		
		response = MtnMomo.collectionRequestToPay(instance.mobile, instance.amount, instance.external_id, instance.payee_note, instance.payer_message, "EUR") # Process Payment through MTN MoMo API
		if isinstance(response,dict):

			instance.transref = response['transaction_ref']
			transdetail = MtnMomo.collectionTransactionStatus(instance.transref)# Get transaction details from MTN MoMo API
			instance.status = transdetail['status']
			instance.financialTransactionId = transdetail['financialTransactionId']
			print(f'Your MoMo request has been successfully processed: {transdetail}')

		else:

			instance.status = 'FAILED'
			print('We had a problem processing request with MTN. Kindly check logs for details')

		instance.processed = True
		instance.save()
