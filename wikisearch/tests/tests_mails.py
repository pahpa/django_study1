# -*- coding: utf-8 -*-
"""
Author: Philippe 'paHpa' Vivien <pahpa@orange.fr>

Copyright: 2022-2023
"""

from django.test import TestCase
from django.core.mail import send_mail

# Create your tests here.


class MailTestCase(TestCase):
    def test_send(self):
        ret = send_mail(
            "Subject here",
            "Here is the message.",
            "messanger@localhost.com",
            ["any@email.com"],
            fail_silently=False,
        )
        self.assertTrue(ret)
