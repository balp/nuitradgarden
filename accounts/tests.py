"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class UserProfile(TestCase):
    def setUp(self):
        self.url = reverse("accounts:profile")
        user = User.objects.create_user("testuser", "test@example.com", "test")
        user.first_name = "Joe"
        user.last_name = "Tester"
        user.save()
        
    def test_profile_should_need_login(self):
        page = self.client.get(self.url)
        self.assertRedirects(page, "accounts/login/?next=%s" % self.url)
        
    def test_logged_in_profile_should_show_username(self):
        self.client.login(username="testuser", password="test")
        page = self.client.get(self.url)
        self.assertContains(page, "testuser")
    
    def test_logged_in_profile_should_show_firstname(self):
        self.client.login(username="testuser", password="test")
        page = self.client.get(self.url)
        self.assertContains(page, "Joe")
        
    def test_logged_in_profile_should_show_lastname(self):
        self.client.login(username="testuser", password="test")
        page = self.client.get(self.url)
        self.assertContains(page, "Tester")

    def test_logged_in_profile_should_show_email(self):
        self.client.login(username="testuser", password="test")
        page = self.client.get(self.url)
        self.assertContains(page, "test@example.com")

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
