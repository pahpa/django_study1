# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""

from django.test import TestCase

# Create your tests here.
from wikisearch.tools.hash import get_hash, check_hash
from wikisearch.tools.dictobj import dict2obj


class ToolsTestCase(TestCase):
    def test_obj(self):
        mydict = dict2obj({"foo": "foo"})
        self.assertIsInstance(mydict, object)

    def test_hash(self):
        url = "https://en.wikipedia.org/w/api.php"
        hurl = get_hash(url)
        self.assertTrue(check_hash(hurl))

        hurl += "Z"
        self.assertFalse(check_hash(hurl))
