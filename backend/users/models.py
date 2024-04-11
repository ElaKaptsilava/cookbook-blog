from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


def user_directory_path(instance, filename):
    return 'user_{0}/profile/{1}'.format(instance.username, filename)


class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField("email address", blank=True, unique=True)
    gender = models.CharField(
        max_length=10, choices=Gender.choices, default=Gender.MALE
    )
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return "{}".format(self.email)

    def __repr__(self):
        return f'CustomUser(email="{self.email}")'


class ChefProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    files = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Recipe Developer: {self.user.username}"
