# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023

example :
./manage.py test wikisearch.tests.tests_wiki
./manage.py test wikisearch.tests.tests_wiki.WikipediaTestCase.test_request_OK
"""
import requests

from django.test import TestCase

# Create your tests here.
from wikisearch.logger import logger
from wikisearch.tools.time import timeit


class WikipediaTestCase(TestCase):
    """
    https://en.wikipedia.org/w/api.php?action=query&titles=Python_(programming_language)&prop=links&pllimit=max
    https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links%7Cextracts&formatversion=2

    """

    # @timeit
    # def test_searchwiki(self):
    #     subject = 'Python (programming language)'
    #     url = 'https://en.wikipedia.org/w/api.php'
    #     params = {
    #             'action':'query',
    #             'format':'json',
    #             'list':'search',
    #             'utf8':1,
    #             'srsearch':subject
    #         }

    #     data = requests.get(url, params=params).json()
    #     logger.debug(data)

    @timeit
    def test_request_OK(self):
        subject = "Python (programming language)"
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": subject,
            "prop": "extracts",
        }

        response = requests.get(url, params=params)
        data = response.json()
        # logger.debug(data)
        page = next(iter(data["query"]["pages"].values()))
        self.assertEqual(page["title"], "Python (programming language)")
        self.assertIn("pageid", page)

    @timeit
    def test_request_KO(self):
        subject = "Klingon (programming language)"
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": subject,
            "prop": "extracts",
        }

        response = requests.get(url, params=params)
        data = response.json()
        # logger.debug(data)
        page = next(iter(data["query"]["pages"].values()))
        self.assertNotIn("pageid", page)

    @timeit
    def test_wikipediapackage(self):
        """
        https://github.com/goldsmith/Wikipedia
        https://stackabuse.com/getting-started-with-pythons-wikipedia-api/
        """
        try:
            import wikipedia

            query = "Python (programming language)"
            response = wikipedia.search(query)
            logger.debug(response)
            # for i in response:
            #     try:
            #         pythonpage = wikipedia.page(i)
            #         logger.debug(f'{pythonpage.title} --> {pythonpage.url}')
            #     except Exception:
            #         pass
            response = wikipedia.page(query).references
            logger.debug(response)
        except Exception:
            logger.warning("NO wikipedia package installed")

    @timeit
    def test_wikipediaAPIpackage(self):
        """
        https://github.com/martin-majlis/Wikipedia-API
        https://stackabuse.com/getting-started-with-pythons-wikipedia-api/
        """
        try:
            import wikipediaapi

            query = "Albert Einstein"
            wiki_wiki = wikipediaapi.Wikipedia("en")
            page_py = wiki_wiki.page(query)
            self.assertTrue(page_py.exists())

            # logger.debug(pformat(page_py.__dict__))
            logger.debug(page_py.fullurl)
            # logger.debug(page_py.summary)

            links = page_py.links
            logger.debug(f"nb links = {len(links)}")
            logger.debug(links)

            for idx, title in enumerate(sorted(links.keys())):
                title.strip(" (id: ??, ns: 0)")
                logger.debug(f"[{idx}] {title}")
                if idx == 9:
                    break

        except Exception:
            logger.warning("NO wikipediaapi package installed")

    # def test_getlink(self):
    #     S = requests.Session()
    #     URL = "https://en.wikipedia.org/w/api.php"
    #     PARAMS = {
    #         "action": "query",
    #         "format": "json",
    #         "titles": "Albert Einstein",
    #         "prop": "links"
    #     }

    #     R = S.get(url=URL, params=PARAMS)
    #     DATA = R.json()

    #     PAGES = DATA["query"]["pages"]

    #     for k, v in PAGES.items():
    #         for l in v["links"]:
    #             #print(l["title"])
    #             logger.debug(l)
