# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""
import logging

logger = logging.getLogger("wikiapi")


def logdebug():
    logger.setLevel(logging.DEBUG)


def loginfo():
    logger.setLevel(logging.INFO)
