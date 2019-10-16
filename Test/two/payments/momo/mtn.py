from mtnmomo.collection import Collection
from mtnmomo.disbursement import Disbursement
from django.conf import settings


class MtnMomo:

	"""This class contains a definition of functions calling the MTN Momo API"""

	collections = Collection(settings.MOMO_HEADER)		
	disbursement= Disbursement(settings.MOMO_HEADER)

	def __init__(self):

		pass

		

	def collectionRequestToPay(mobile,amount,payid,paynote,paymsg,currency):

		"""This method initiates a request to pay Collection to mtn"""

		try:

			return MtnMomo.collections.requestToPay(mobile=mobile, amount=amount, external_id=payid, payee_note=paynote, payer_message=paymsg, currency=currency)
		 
		except Exception as e:

			return e

	def collectionTransactionStatus(referenceId):

		"""This method returns the status of a Collection transaction using the transfer id"""
		try:

			return MtnMomo.collections.getTransactionStatus(referenceId)

		except Exception as e:

			return e

	def disbursementTransfer(amount,mobile,external_id,payee_note="",payer_message="",currency="EUR"):

		"""This method initiates a request to transfer payment to mtn"""

		try:

			return MtnMomo.disbursement.transfer(amount=amount, mobile=mobile, external_id=external_id, payee_note=payee_note,payer_message=payer_message, currency=currency)


		except Exception as e:

			return e

	def disbursementTransactionStatus(referenceId):

		"""This method returns the status of a Disbursement transaction using the transfer id"""

		try:

			return MtnMomo.disbursement.getTransactionStatus(referenceId)

		except Exception as e:

			return e



		