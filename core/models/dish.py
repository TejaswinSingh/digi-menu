from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Dish(models.Model):
    MIN_RATING = Decimal('0.0')
    MAX_RATING = Decimal('5.0')

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[
            MinValueValidator(Decimal('1.00')),
            MaxValueValidator(Decimal('9999.99'))   # max price of a dish can be 9999.99
        ],
    )
    rating = models.DecimalField(
        max_digits=2, decimal_places=1,
        validators=[
            MinValueValidator(MIN_RATING),
            MaxValueValidator(MAX_RATING)
        ],
        default=Decimal('0.0')    
    )
    picture = models.URLField(default='', blank=True)

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name
    
    def update_rating(self):
        n = 0
        sum = 0
        for r in self.ratings.all():
            sum += r.value
            n += 1

        average_rating = Decimal(f'{sum / n:.1f}')
        self.rating = average_rating
        self.save()