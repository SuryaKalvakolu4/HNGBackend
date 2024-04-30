from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()


class AccountTests(TestCase):
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


    def test_get_user_list(self):
        list_url = reverse("accounts:list")

        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        response = self.client.get(list_url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_register(self):
        register_url = reverse("accounts:register")

        # List of required fields
        required_fields = [
            "password",
            "email",
            "username",
            "born_year",
            "gender",
            "is_student",
            "country",
            "state",
            "city"
        ]

        for field in required_fields:
            with self.subTest(field=field):
                # Create a data dictionary with all fields empty
                data = {
                    "password": "testpassword",
                    "email": "user@gmail.com",
                    "username": "testuser",
                    "born_year": 2001,
                    "gender": "male",
                    "is_student": True,
                    "country": "Test Country",
                    "state": "Test State",
                    "city": "Test City"
                }
#console.log
                # Set the current field to an empty string
                data[field] = ""
                data["university_name"] = "Test University"

                response = self.client.post(register_url, data)

                # Assert that the response status code is 400 (validation error)
                self.assertEqual(response.status_code, 400)

                # checking if the code of the error message is blank or invalid
                self.assertIn(response.data[field][0].code, ["blank", "invalid"])
        
        # testing if a user is student but doesn't enter university_name
        data["city"] = "Test City"
        data["university_name"] = ""
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["university_name"][0].code, "university_name is required")

        # testing if register_url works with correct data
        data["university_name"] = "Test University"
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, 201)
        new_user = User.objects.get(id=response.data["id"])

        # activating account
        self.assertEqual(new_user.is_active, False)
        activation_token = response.data["activation_token"]
        activation_url = reverse("accounts:activate", args=[activation_token])
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, 200)

        # Refresh the user from the database
        new_user.refresh_from_db()

        # after requesting activation_url the is_active field of the new_user must be True
        self.assertEqual(new_user.is_active, True)

        # testing unique email exception
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["email"][0].code, "unique")

        # testing unique username exception
        data["email"] = "user2@gmail.com"
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["username"][0].code, "unique")


    def test_log_out(self):
        logout_url = reverse("accounts:logout")
        data = {'refresh_token': self.refresh_token}
        response = self.client.post(logout_url, data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["detail"], "Logout successful")
