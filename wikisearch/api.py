# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from typing import List

from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from ninja import Schema
from ninja.pagination import paginate

from .models import WikiUrlLog

api = NinjaAPI()


class WikiUrlLogOut(Schema):
    id: int
    url: str
    param: str = None
    summary: str = None
    link: List[str] = None

    def resolve_link(self, obj):
        return obj.get_links()


@api.get("/wikilogs", response=List[WikiUrlLogOut])
@paginate
def list__wikilog(request):
    qs = WikiUrlLog.objects.all()
    return qs


@api.get("/wikilog/{wikilog_id}", response=WikiUrlLogOut)
def details_wikilog(request, wikilog_id: int):
    obj = get_object_or_404(WikiUrlLog, pk=wikilog_id)
    return obj
