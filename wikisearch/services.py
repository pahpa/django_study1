# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
import wikipediaapi

from django.core.mail import send_mail

from .models import WikiUrlLog, WikiLink
from .logger import logger


def fetch_wiki(datasearch, lang="en"):
    wiki_wiki = wikipediaapi.Wikipedia(lang)
    page_wiki = wiki_wiki.page(datasearch)
    if page_wiki.exists():
        logger.debug(f"page_wiki.fullurl: {page_wiki.fullurl}")
        return page_wiki
    return None


def parse_wiki(page_wiki):
    links = page_wiki.links
    logger.debug(f"nb links = {len(links)}")
    linklist = []
    for idx, title in enumerate(links.keys()):
        title.strip(" (id: ??, ns: 0)")
        linklist.append(title)
        # if idx == 9: break

    return {
        "fullurl": page_wiki.fullurl,
        "title": page_wiki.title,
        "summary": page_wiki.summary,
        "linklist": linklist,
    }


def save_wiki(urlsearch, param, wikidata):
    try:
        objw, created = WikiUrlLog.objects.get_or_create(
            url=urlsearch,
            defaults={
                "param": param,
                "summary": wikidata.get("summary") if wikidata is not None else None,
                "fullurl": wikidata.get("fullurl") if wikidata is not None else "",
                "httpstatus": 200 if wikidata is not None else 404,
            },
        )

        if created:
            logger.info(wikidata)
            logger.info(wikidata.keys())
            lstlink = wikidata.get("linklist") if wikidata is not None else None
            if lstlink:
                for linkinfo in lstlink:
                    try:
                        objlink, created = WikiLink.objects.get_or_create(link=linkinfo)
                        objlink.wikis.add(objw)
                        objlink.save()
                    except Exception as e:
                        logger.error(e)

    except Exception as e:
        logger.error(f"{urlsearch}: {e}")


def mail_wikilog(r, nb):
    logger.info(f"{r} Sending Mail wikilink > 100")
    send_mail(
        f"Warning wikilog {r} > 100",
        f"blabla: Warning wikilog {r} as {nb} links...",
        "messanger@localhost.com",
        ["any@email.com"],
        fail_silently=False,
    )
