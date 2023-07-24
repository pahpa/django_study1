# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from django.contrib import admin
from django.db.models.fields.json import JSONField
from django.utils.html import format_html
from jsoneditor.forms import JSONEditor

# Register your models here.
from .models import WikiUrlLog, WikiLink


@admin.register(WikiUrlLog)
class AdminWikiUrlLog(admin.ModelAdmin):
    list_display = ("id", "url", "param", "summary", "show_link_fullurl")
    list_filter = ("httpstatus",)
    search_fields = ("url", "summary")

    formfield_overrides = {
        JSONField: {"widget": JSONEditor},
    }

    def show_link_fullurl(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.fullurl)


@admin.register(WikiLink)
class AdminWikiLink(admin.ModelAdmin):
    list_display = ("id", "link", "get_wikis")
    # raw_id_fields = ("wikis",)
    search_fields = ("link",)

    def get_wikis(self, obj):
        return ", ".join([p.param for p in obj.wikis.all()])
