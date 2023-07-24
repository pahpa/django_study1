# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
import urllib.parse


def get_baseurl(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path = "/".join(parsed.path.split("/")[:-1]) if with_path else ""
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params="")
    parsed = parsed._replace(query="")
    parsed = parsed._replace(fragment="")
    return parsed.geturl()
