from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import authenticate


from .models import UserModels


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = UserModels
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'birthday',
            'gender', 'phone', 'address', 'country', 'city', 'state', 'password', 'avatar', 'is_vlad'
        ]
        read_only_fields = ['password']

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance



class RegistrationUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        style={'input_type': 'password'},
        write_only=True
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    token = serializers.CharField(
        max_length=256,
        read_only=True
    )
    avatar = serializers.FileField(
        max_length=20, allow_empty_file=True, use_url=True, required=False, allow_null=True)

    class Meta:
        model = UserModels
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'birthday', 'gender', 'phone',
            'address', 'country', 'city', 'state', 'password', 'password2', 'token', 'avatar',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '')

        if not email:
            raise serializers.ValidationError(
                'User should have email')
        return attrs

    def create(self, validated_data):
        account = UserModels(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            birthday=self.validated_data['birthday'],
            gender=self.validated_data['gender'],
            phone=self.validated_data['phone'],
            address=self.validated_data['address'],
            country=self.validated_data['country'],
            city=self.validated_data['city'],
            state=self.validated_data['state'],
            avatar=self.validated_data['avatar'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
                'password': 'Passwords must match.'
            })
        account.set_password(password)
        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=256)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=256, read_only=True)
    is_vlad = serializers.BooleanField(read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = get_object_or_404(UserModels, email=email)

        if not user.is_active:
            raise serializers.ValidationError(
                'Account is not activated, please check your email and click the link to activate.'
            )

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found or has been banned.'
            )

        return user