# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
import django
from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule

from wikisearch.logger import logger

django.setup()


class Command(BaseCommand):
    help = "Create Celery Data Config"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            dest="force",
            default=False,
            help="Delete and Create",
        )

    def handle(self, *args, **options):
        if options["force"]:
            logger.info("Deleting...")
            CrontabSchedule.objects.all().delete()

        CrontabSchedule(**{
            "minute": "*",
            "hour": "*",
            "day_of_week": "*",
            "day_of_month": "*",
            "month_of_year": "*",
            "day_of_week": "*"}).save()

        logger.info("OK")
