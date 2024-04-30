
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from accounts.models import MyUser as User
from decouple import config
import random
from rest_framework.exceptions import AuthenticationFailed


def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(
                email=email, password=config('SOCIAL_SECRET'))

            return {
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'email': email,
            'password': config('SOCIAL_SECRET')}
        user = User.objects.create_user(**user)
        user.auth_provider = provider
        user.save()
        if check_password(config('SOCIAL_SECRET'), user.password):
            # Passwords match, proceed with authentication
            new_user = user
        return {
            'email': new_user.email,
            'tokens': new_user.tokens()
        }
