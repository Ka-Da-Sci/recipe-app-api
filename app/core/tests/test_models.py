"""Tests for models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_success(self):
        """Test that creating a user with an email is successful."""

        email = "karl@example.com"
        password = "pass12345"
        name = "Test User"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email for a new user is normalized."""

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            with self.subTest(email=email):
                user = get_user_model().objects.create_user(
                       email, 'sample0987')
                self.assertEqual(user.email, expected)

    def test_new_user_without_email(self):
        """Test creating user without email raises error."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'saample5436')

    def test_user_model_without_name(self):
        """Test creating user without name raises error."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='ekom@example.com',
                                                 password='sample985jf',
                                                 name='')

    def test_create_new_superuser(self):
        """Test creating a new superuser."""

        user = get_user_model().objects.create_superuser(
            'karl999@example.com', 'sample5nnvj6')
        self.assertTrue(user.is_superuser, msg="Superuser flag should be True")
        self.assertTrue(user.is_staff, msg="Staff flag should be True")
