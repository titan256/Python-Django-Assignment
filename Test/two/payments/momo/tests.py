from django.test import TestCase
from .models import MomoRequest
from .mtn import MtnMomo

# Create your tests here.
class MtnMoMoTestCase(TestCase):

	def setUp(self):
		pass

	def test_get_transaction_status(self):

		status = MtnMomo.collectionTransactionStatus('7858409e-fd71-48b9-a1a5-ca22eb9c6bfd')
		assert isinstance(status, dict)
		assert "amount" in status.keys()
		assert "currency" in status.keys()

	def test_request_to_pay(self):

		ref = MtnMomo.collectionRequestToPay("256772123456", "600", "123456789", "dd","dd","EUR")
		assert isinstance(ref, dict)
		assert "transaction_ref" in ref.keys()