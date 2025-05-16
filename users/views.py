from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


@extend_schema(summary="Register a new user", tags=["Auth"])
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [
        AllowAny,
    ]
