# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from django.db import models
from django.urls import reverse
from django.db.models import Count

APP = "wikisearch"
# Create your models here.


class WikiModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = APP
        abstract = True

    def __str__(self):
        return f"(C:{self.created_at} U:{self.updated_at})"

    def get_admin_url(self):
        return reverse(
            "admin:{0}_{1}_change".format(self._meta.app_label, self._meta.model_name),
            args=(self.pk,),
        )

    @classmethod
    def get_duplicate(cls, order_name):
        return (
            cls.objects.values(order_name)
            .annotate(Count("id"))
            .order_by(order_name)
            .filter(id__count__gt=1)
        )


class WikiUrlLog(WikiModel):
    url = models.URLField(max_length=200, db_index=True)
    param = models.CharField(max_length=100, blank=True, db_index=True)
    summary = models.JSONField(blank=True, null=True, db_index=True)
    fullurl = models.URLField(max_length=200, blank=True, db_index=True)
    httpstatus = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = APP
        ordering = ["url"]

    def __str__(self):
        return f"{self.url}"

    def get_links(self):
        return list(self.wikilink_set.all().values_list("link", flat=True))


class WikiLink(WikiModel):
    link = models.CharField(max_length=200, db_index=True)
    url = models.URLField(max_length=200, blank=True, db_index=True)
    wikis = models.ManyToManyField(WikiUrlLog)

    class Meta:
        app_label = APP

    def __str__(self):
        return f"{self.link}"
