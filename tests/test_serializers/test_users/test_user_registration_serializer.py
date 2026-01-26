from django.test import TestCase
from django.contrib.auth import get_user_model
from users.serializers import UserRegistrationSerializer

User = get_user_model()


class UserRegistrationSerializerTest(TestCase):
    def test_valid_registration(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "securepass123",
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        user = serializer.save()

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, "newuser")
        self.assertEqual(user.email, "newuser@example.com")
        self.assertTrue(user.check_password("securepass123"))

    def test_missing_username(self):
        data = {"email": "missing@example.com", "password": "somepass"}
        serializer = UserRegistrationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_password_is_write_only(self):
        serializer = UserRegistrationSerializer()
        self.assertTrue(serializer.fields["password"].write_only)
