from django.db import models
from users.models import CustomUser

from recipes_manager.models import Recipe


def user_directory_path(instance, filename):
    user_email = instance.user.email if instance.user else 'unknown_user'
    return f"user_{user_email}/ratings/{filename}"


class Review(models.Model):
    comment = models.TextField()
    image = models.ImageField(upload_to=user_directory_path)
    date = models.DateField()


class AbstractReview(Review):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Rating(AbstractReview):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    class Meta:
        unique_together = ('recipe', 'custom_user')

    def __str__(self):
        return f"Rating for {self.recipe.title} by {self.custom_user.username}"

    def __repr__(self):
        return (f"Rating(pk={repr(self.pk)}, recipe={repr(self.recipe.title)}, user={repr(self.custom_user.username)}, "
                f"rate={repr(self.rate)})")
