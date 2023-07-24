# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from random_word import RandomWords
from enum import Enum
import random

import django
from django.core.management.base import BaseCommand

from wikisearch.models import WikiUrlLog
from wikisearch.logger import logger

django.setup()


class LoremKind(Enum):
    SENTENCE = 1
    PARAGRAPH = 2


class Command(BaseCommand):
    help = "Create Fake Data Search"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            dest="force",
            default=False,
            help="Delete and Create",
        )

    def set_data(self, word="NULL", kind=LoremKind.PARAGRAPH):
        try:
            import lorem

            if kind == LoremKind.PARAGRAPH:
                return lorem.paragraph()
            elif kind == LoremKind.SENTENCE:
                return lorem.sentence()
        except Exception:
            return f"blabla {word}"

    def handle(self, *args, **options):
        if options["force"]:
            logger.info("Deleting...")
            WikiUrlLog.objects.all().delete()

        if WikiUrlLog.objects.all().count() < 101:
            logger.info("Creating...")
            r = RandomWords()

            for i in range(0, random.randrange(1, 30)):
                word = r.get_random_word()
                url = f"http://localhost:8000/wikipedia_search?query={word}"

                obj, created = WikiUrlLog.objects.get_or_create(
                    url=url,
                    defaults={
                        "param": f"{word}",
                        "summary": self.set_data(LoremKind.SENTENCE),
                        "fullurl": f"https://en.wikipedia.org/wiki/{word}",
                        "httpstatus": random.choice([200, 400, 500]),
                    },
                )

        logger.info("OK")
