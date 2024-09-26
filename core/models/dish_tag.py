from django.db import models
from core.models import (
    Dish,
    Tag
)


class DishTag(models.Model):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name='tags'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='dishes'
    )

    class Meta:
        verbose_name_plural = 'Dish Tags'
        constraints = [
            models.UniqueConstraint(
                fields=['dish', 'tag'],
                name='%(app_label)s_%(class)s_unique'
            )
        ]

    def __str__(self):
        return f"{self.dish} [{self.tag}]"