from django.test import TestCase
from .models import PlatformUser

class PlatformUserTests(TestCase):
    def test_email_is_username_field(self):
        self.assertEqual(PlatformUser.USERNAME_FIELD, "email")
