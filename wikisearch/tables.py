# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
import django_tables2 as tables
from django_tables2.utils import A

from .models import WikiUrlLog, WikiLink


class WikiUrlLogTable(tables.Table):
    id = tables.LinkColumn("wikilogdetails", args={A("pk")})

    class Meta:
        model = WikiUrlLog
        exclude = ("created_at", "updated_at", "url", "httpstatus")


class WikiLinkTable(tables.Table):
    class Meta:
        model = WikiLink
