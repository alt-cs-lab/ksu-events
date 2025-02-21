# registration/tests/test_model_users.py
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword123'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='testuser2',
                email='testuser@example.com',
                password='testpassword123'
            )