import unittest
from .. import models
from What_is_mem.api.v1.views import SignIn
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User

class TestLogIn(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="test", password="test123")
        self.view = SignIn()

    def test_login_get(self):
        request = self.factory.get("/login/")
        response = self.view.saver(request)
        self.assertIsInstance(response, dict)
        self.assertEqual(response, {})

    def test_login_post_success(self):
        request = self.factory.post("/login/", {"username": "test", "password": "test123"})
        request.user = self.user
        response = self.view.login(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

    def test_login_post_failure(self):
        request = self.factory.post("/login/", {"username": "foo", "password": "bar"})
        response = self.view.login(request)
        self.assertIsInstance(response, dict)
        self.assertEqual(response, {"error": "Неверное имя пользователя или пароль"})