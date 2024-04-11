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


class CommunityOpinion(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, help_text='Your email address.')
    first_name = models.CharField(max_length=50, help_text='Your first name.')
    last_name = models.CharField(max_length=50, help_text='Your last name.')
    opinion = models.TextField(help_text='Your opinion about the recipe.')
    date = models.DateField(auto_now_add=True, help_text='Date when the opinion was added.')

    class Meta:
        unique_together = ('email', 'recipe')

    def __str__(self):
        return f'Opinion for by {self.email}'

    def __repr__(self):
        return f'CommunityOpinion(email={self.email!r}'
