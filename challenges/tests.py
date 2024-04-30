from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Challenge


User = get_user_model()


class ChallengeTests(TestCase):
    def setUp(self):
        # Set up any initial data or configurations for your tests
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@test.com', password='testpassword')
        login_data = {          # Example: authenticate the client
            "email": self.user.email,
            "password": "testpassword"
        }
        login_response = self.client.post(reverse('accounts:login'), login_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.access_token = login_response.data['access']
        self.refresh_token = login_response.data['refresh']
        self.headers = {'Authorization': f'Bearer {self.access_token}'}
        self.challenge = Challenge.objects.create(
            day = "Challenge day 1"
        )


    def test_get_challenge(self):
        challenge_detail_url = reverse("challenges:detail", args=[self.challenge.day])

        response = self.client.get(challenge_detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        response = self.client.get(challenge_detail_url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["day"], self.challenge.day)
