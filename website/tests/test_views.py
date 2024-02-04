from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class HomePageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create_user(username="testuser", password="12345")

    def setUp(self):
        self.client.login(username="testuser", password="12345")

    def test_instance_creation(self):
        user = User.objects.get(id=1)
        self.assertTrue(isinstance(user, User))

    def test_login_works_properly(self):
        response = self.client.get("/")

        self.assertEqual(response.context["user"].username, "testuser")

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("home"))
        self.assertRedirects(response, "/accounts/login/?next=/")

    def test_home_page_url_exists(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_home_page_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy("home"))

        self.assertEqual(response.status_code, 200)
