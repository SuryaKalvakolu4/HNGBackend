from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from .models import Event
from .utils import create_test_event


User = get_user_model()


class EventTests(TestCase):
    def setUp(self):
        # Set up any initial data or configurations for your tests
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@test.com', password='testpassword')
        login_data = {          # Example: authenticate the client
            "email": self.user.email,
            "password": "testpassword"
        }
        self.event = create_test_event()
        login_response = self.client.post(reverse('accounts:login'), login_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.access_token = login_response.data['access']
        self.refresh_token = login_response.data['refresh']
        self.headers = {'Authorization': f'Bearer {self.access_token}'}

    def test_event_signup(self):
        event_signup_url = reverse("events:sign-up", args=[self.event.id])
        data = {
            "user": self.user.id
        }
        response = self.client.get(event_signup_url, data=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)

        # testing if the event is added to the user
        self.user.refresh_from_db()
        self.assertEqual(self.user.events.all().count(), 1)

        # testing with unauthorized user (without sending access_token in headers)
        response = self.client.get(event_signup_url, data=data)
        self.assertEqual(response.status_code, 401)
