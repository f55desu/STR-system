from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', surname='Christ', name='Jesus', lastname=None, password='foo')

        self.assertEqual(user.email, 'normal@user.com')

        self.assertEqual(user.surname, 'Christ')
        self.assertEqual(user.name, 'Jesus')
        self.assertIsNone(user.lastname)

        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option

            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', surname='Christ', name='Jesus', lastname=None, password='foo')

        self.assertEqual(admin_user.email, 'super@user.com')

        self.assertEqual(admin_user.surname, 'Christ')
        self.assertEqual(admin_user.name, 'Jesus')
        self.assertIsNone(admin_user.lastname)

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option

            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)