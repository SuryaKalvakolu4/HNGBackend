import random
import string

from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


def code_slug_generator(size=12, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))


def create_slug_shortcode(size, model_):
    new_code = code_slug_generator(size=size)
    qs_exists = model_.objects.filter(slug=new_code).exists()
    if qs_exists:
        return create_slug_shortcode(size, model_)
    return new_code


def generate_code(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_activation_code(model_, size=6):

    code = generate_code(size)

    if model_.objects.filter(activation_code=code).exists():
        return create_activation_code(size)

    return code


def send_email(to_email, token, domain, email_type="register"):

    activation_link = reverse('accounts:activate', args=[token])

    if email_type == "register":
        title = 'Activate Your Account'
        content = f'Click the following link to activate your account: {domain}{activation_link}'
    elif email_type == "forgot_pass":
        title = 'Reset your password'
        content = f'Click the following link to reset your password: {domain}{activation_link}'

    send_mail(
        title,
        content,
        settings.DEFAULT_FROM_EMAIL,
        [to_email,],
        fail_silently=True
    )
