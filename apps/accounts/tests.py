from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from apps.accounts.views.signup import SignupPageView
from apps.accounts.forms.signup import CustomUserCreationForm


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        Test creating a new superuser.
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        self.url = reverse('signup')
        self.response = self.client.get(self.url)

    def test_signup_page(self):
        """
        Test signup page response, template and view name.
        """
        with self.subTest(name="response status code"):
            self.assertEqual(self.response.status_code, 200)

        with self.subTest(name="template used"):
            self.assertTemplateUsed(
                self.response, 'registration/signup.html')

        with self.subTest(name="content not contains"):
            self.assertNotContains(
                self.response, 'Hi there! I should not be on the page.')

        with self.subTest(name="form instance"):
            form = self.response.context.get('form')
            self.assertIsInstance(form, CustomUserCreationForm)

        with self.subTest(name="csrf token"):
            self.assertContains(self.response, 'csrfmiddlewaretoken')

        with self.subTest(name="view function"):
            view = resolve('/accounts/register/')
            self.assertEqual(
                view.func.__name__,
                SignupPageView.as_view().__name__
            )
