# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from pprint import pformat

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from django.urls import reverse

from django_tables2 import RequestConfig
from .models import WikiUrlLog
from .tables import WikiUrlLogTable, WikiLinkTable
# from .filters import WikiUrlLogFilter
from .logger import logger
from .services import fetch_wiki, parse_wiki, save_wiki


def index(request):
    qs = WikiUrlLog.objects.all()
    table = WikiUrlLogTable(qs)
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(request, "index.html", {"table": table})


def wikipedia_search(request):
    if request.method == "GET":
        logger.debug(pformat(request.GET))
        if "query" not in request.GET:
            logger.error("mandatory query param")
        else:
            if len(request.GET.get("query")):
                query = request.GET.get("query")
                retpage = fetch_wiki(query)
                retdata = None
                if retpage:
                    retdata = parse_wiki(retpage)
                save_wiki(request.build_absolute_uri(), query, retdata)
    return HttpResponseRedirect(reverse("wikiindex"))


def wikilog_details(request, id):
    obj = get_object_or_404(WikiUrlLog, pk=id)
    table = WikiLinkTable(obj.wikilink_set.all())
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(
        request, "wikilog_details.html", {"wiki": obj, "links": table}
    )
