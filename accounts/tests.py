from django.test import TestCase

from .models import CustomUser


class CustomUserTests(TestCase):
    """
    Tests for the creation of users
    """

    def test_custom_user(self):
        """
        Test for the creation of a normal user
        """
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testPassword',
        )

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_custom_admin_user(self):
        """
        Test for the creation of an admin user
        """
        admin_user = CustomUser.objects.create_superuser(
            username='adminuser',
            email='admin@email.com',
            password='adminPassword'
        )

        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'admin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
