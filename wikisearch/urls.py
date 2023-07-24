# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from django.urls import path

from . import views
from .api import api

urlpatterns = [
    path("", views.index, name="wikiindex"),
    path("wikipedia_search", views.wikipedia_search, name="wikipediasearch"),
    path("wikilog_details/<int:id>", views.wikilog_details, name="wikilogdetails"),
    path("swagger/", api.urls),
]
