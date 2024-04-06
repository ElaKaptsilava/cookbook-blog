from django.db import models
from django.contrib.auth.models import User

from users.models import CustomUser


def user_directory_path(instance, filename):
    user_email = instance.user.email if instance.user else 'unknown_user'
    return f"user_{user_email}/reviews/{filename}"


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    comment = models.TextField()
    image = models.ImageField(upload_to=user_directory_path)
    date = models.DateField()

    class Meta:
        abstract = True


class AbstractReview(Review):
    class Meta:
        abstract = True
        unique_together = ('recipe', 'user')


class Rating(AbstractReview):
    rate = models.PositiveIntegerField()

    def __str__(self):
        return f"Rating for {self.recipe.title} by {self.user.username}"

    def __repr__(self):
        return (f"Rating(pk={repr(self.pk)}, recipe={repr(self.recipe.title)}, user={repr(self.user.username)}, "
                f"rate={repr(self.rate)})")


class Recipe(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
