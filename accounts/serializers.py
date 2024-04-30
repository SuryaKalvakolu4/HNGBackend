from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    born_year = serializers.IntegerField(required=True)
    username = serializers.CharField(max_length=100, required=True)
    gender = serializers.CharField(max_length=10, required=True)
    is_student = serializers.BooleanField(required=True)
    university_name = serializers.CharField(max_length=100, required=False)
    country = serializers.CharField(max_length=50, required=True)
    state = serializers.CharField(max_length=50, required=True)
    city = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = MyUser
        fields = "__all__"
        extra_kwargs = {
            'slug': {'read_only': True},
            'is_active': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_staff': {'read_only': True},
            'last_login': {'read_only': True},
            'reset_code': {'read_only': True},
            'activation_token': {'read_only': True},
            'events': {'read_only': True},
            'auth_provider': {'read_only': True},
            'medals': {'read_only': True},
        }

    def validate(self, attrs):
        username = attrs.get("username")
        user = MyUser.objects.filter(username=username)
        # validating if a user with this username exists
        if user:
            if user.first().is_active:
                raise ValidationError(
                    {"username": "This username has already been registered"}, "unique")
            else:
                user.first().delete()

        is_student = attrs.get("is_student")
        university_name = attrs.get("university_name")
        if is_student and not university_name:
            raise ValidationError(
                    {"university_name": "Please enter your university name"}, "university_name is required")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class PasswordForgotSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordForgotConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)


class RegionSerializer(serializers.Serializer):
    name = serializers.CharField()
