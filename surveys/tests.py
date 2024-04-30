from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from .utils import create_test_challenge
from prizes.models import Medal
from .models import Survey


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
        login_response = self.client.post(reverse('accounts:login'), login_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.access_token = login_response.data['access']
        self.refresh_token = login_response.data['refresh']
        self.headers = {'Authorization': f'Bearer {self.access_token}'}
        Medal.objects.create(name="Bronze")
        Medal.objects.create(name="Silver")
        Medal.objects.create(name="Gold")

    def test_create_survey(self):
        create_survey_url = reverse("surveys:create")
        data = {
            "user": self.user.id,
            "challenge": create_test_challenge().id,
            "physical_done": "",
            "mental_done": "",
            "social_done": "",
            "video_on_ig": "",
            "video_link": "",
        }
        my_user = self.user

        # testing with unauthorized user (without sending access_token in headers)
        response = self.client.post(create_survey_url, data=data)
        self.assertEqual(response.status_code, 401)

        # testing with authorized user
        response = self.client.post(create_survey_url, data=data, headers=self.headers)
        self.assertEqual(response.status_code, 400)

        data = {
            "challenge": create_test_challenge().id,
            "physical_done": True,
            "mental_done": True,
            "social_done": True,
            "video_on_ig": True,
            "video_link": "https://www.instagram.com/",
        }
        response = self.client.post(create_survey_url, data=data, headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(my_user.medals.all().count(), 0)

        # testing if the bronze medal is added after completing minimum 37 tasks
        # in this case, after the loop there will be 13 survey with 3 completed tasks for each
        # and it makes 13*3=39 challenges, so the user must get the Bronze medal
        for _ in range(12):
            response = self.client.post(create_survey_url, data=data, headers=self.headers)
        self.assertEqual(my_user.medals.all().count(), 1)
        self.assertEqual(my_user.medals.all().last().name, "Bronze")

        # we create new 4 survey here (4*3=12 new completed challenges) and
        # total number of completed challenges will be 39+12=51, which means
        # the user must earn Silver medal
        for _ in range(4):
            response = self.client.post(create_survey_url, data=data, headers=self.headers)
        self.assertEqual(my_user.medals.all().count(), 2)
        self.assertEqual(my_user.medals.all().last().name, "Silver")

        # 2 more survey here (2*3=6 new completed challenges) and
        # total number of completed challenges will be 51+6=57, which means
        # the user must earn Gold medal
        for _ in range(2):
            response = self.client.post(create_survey_url, data=data, headers=self.headers)
        self.assertEqual(my_user.medals.all().count(), 3)
        self.assertEqual(my_user.medals.all().last().name, "Gold")
