from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from core.models import (
    Dish,
    User
)
from decimal import Decimal


class DishRating(models.Model):
    MIN_RATING = Decimal('1.0')
    MAX_RATING = Decimal('5.0')

    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="dish_ratings"
    )
    value = models.DecimalField(
        max_digits=2, decimal_places=1,
        validators=[
            MinValueValidator(MIN_RATING),
            MaxValueValidator(MAX_RATING)
        ], 
    )

    class Meta:
        verbose_name_plural = 'Dish Ratings'
        constraints = [
            models.UniqueConstraint(
                fields=['dish', 'user'],   # a user can rate a dish only once
                name='%(app_label)s_%(class)s_unique'
            )
        ]

    def __str__(self):
        return f"{self.user} on {self.dish}"


@receiver(post_save, sender=DishRating)
def update_dish_rating(sender, instance, created, **kwargs):
    instance.dish.update_rating()