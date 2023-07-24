# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from rest_framework import serializers

from .models import WikiUrlLog


class WikiUrlLogSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    def get_links(self, wwikiurllog):
        return list(wwikiurllog.wikilink_set.all().values_list("link", flat=True))

    class Meta:
        fields = "__all__"
        model = WikiUrlLog
