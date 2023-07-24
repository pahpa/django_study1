# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from django.test import TestCase

# Create your tests here.
from wikisearch.models import WikiUrlLog


class ModelTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.url = "htpp://localhost:8000/wikisearch/wikipedia_search?query=blabla|foo"

        obj = WikiUrlLog.objects.create(url=self.url, param="foo")
        self.assertIsInstance(obj, WikiUrlLog)

    def test_get_or_create(self):
        from random_word import RandomWords

        r = RandomWords()

        for i in range(0, 10):
            url = f"htpp://localhost:8000/wikisearch/wikipedia_search?query={r.get_random_word()}"
            obj, created = WikiUrlLog.objects.get_or_create(
                url=url,
                defaults={
                    "param": "blabla",
                    "summary": "foo",
                    "fullurl": "http://foo.io",
                    "httpstatus": 200,
                },
            )
            self.assertIsInstance(obj, WikiUrlLog)

    def test_getadminurl(self):
        q = WikiUrlLog.objects.get(pk=1)
        self.assertEqual(q.get_admin_url(), "/admin/wikisearch/wikiurllog/1/change/")

    def test_getobjets(self):
        q = WikiUrlLog.objects.all()
        self.assertEqual(len(q), 1)
