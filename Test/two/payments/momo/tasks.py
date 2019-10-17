import logging
from .models import MomoRequest
from payments.celery import app
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .mtn import MtnMomo

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/1')), name="payment_status_task", ignore_result=True)
def get_payment_status_task():

	momorequests = MomoRequest.objects.exclude(status="SUCCESSFUL")

	for request in momorequests:

	    transdetail = MtnMomo.collectionTransactionStatus(request.transref)
	    request.status = transdetail['status']
	    request.save()
	    logger.info(transdetail)



