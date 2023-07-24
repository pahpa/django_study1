# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from django_filters import FilterSet

from .models import WikiUrlLog


class WikiUrlLogFilter(FilterSet):
    class Meta:
        model = WikiUrlLog
        fields = {"param": ["exact", "contains"]}
