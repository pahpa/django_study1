# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from random_word import RandomWords

from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from unittest.mock import patch

# Create your tests here.


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.r = RandomWords()
        self.baseurl = reverse("wikipediasearch")
        self.url = f"{self.baseurl}?query="

    @patch("wikisearch.views.fetch_wiki")
    @patch("wikisearch.views.parse_wiki")
    @patch("wikisearch.views.save_wiki")
    def test_wiki(self, mock_save_wiki, mock_parse_wiki, mock_fetch_wiki):
        query = "Python (programming language)"
        simulated_retpage = "Simulated Wikipedia page content."
        simulated_retdata = "Simulated parsed data."

        mock_fetch_wiki.return_value = simulated_retpage
        mock_parse_wiki.return_value = simulated_retdata

        query = "Python (programming language)"
        response = self.client.get(self.url, {"query": query})

        mock_fetch_wiki.assert_called_once_with(query)
        mock_parse_wiki.assert_called_once_with(simulated_retpage)
        mock_save_wiki.assert_called_once_with(
            response.wsgi_request.build_absolute_uri(),
            query,
            simulated_retdata)

        self.assertRedirects(response, reverse("wikiindex"))

    def _test_getrandomquery(self):
        response = self.client.get(f"{self.url}{self.r.get_random_word()}")
        self.assertEqual(response.status_code, 302)
