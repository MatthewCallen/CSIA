from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
import os


class PremDataBaseConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY,'abc123')
        try:
            do_something
        except Exception as e:
            self.fail(e)