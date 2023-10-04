# Create your tasks here

from celery import shared_task

from django.db.models import Count

from .models import WikiUrlLog
from .logger import logger
from .services import mail_wikilog


@shared_task(name="wikilog_count")
def check_wikilog_count():
    logger.info("WikiUrlLog...")

    for r in (
        WikiUrlLog.objects.all()
        .annotate(link_count=Count("wikilink"))
        .filter(link_count__gt=100)
    ):
        mail_wikilog(r, r.link_count)
