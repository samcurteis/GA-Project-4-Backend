from rest_framework.test import APITestCase
from django.urls import reverse

from .. import views 

class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")

        user_data = {
                'email':"email@gmail.com",
                'first_name': "First",
                'last_name': "Last",
                'profile_image': "profileImage",
                'password': "Password!1"
                }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
