# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
from hashlib import blake2b
import json
import string


def get_hash(item):
    if isinstance(item, str):
        string = item

    elif isinstance(item, dict):
        # sort_keys is recursive
        string = json.dumps(item, sort_keys=True)

    else:
        raise TypeError(f"L'objet de type {type(item)} n'est pas hashable")

    h = blake2b(digest_size=20)
    h.update(string.encode("utf-8"))
    return h.hexdigest()


def check_hash(data):
    if isinstance(data, bytes):
        # only decodes utf-8 string
        try:
            data = data.decode()
        except ValueError:
            return False
    return isinstance(data, str) and all(c in string.hexdigits for c in data)
