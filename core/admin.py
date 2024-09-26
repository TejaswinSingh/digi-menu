from django.contrib import admin
from core.models import (
    User, UserAdmin,
    Dish,
    DishRating,
    Tag,
    DishTag
)

admin.site.register(User, UserAdmin)
admin.site.register(Dish)
admin.site.register(DishRating)
admin.site.register(Tag)
admin.site.register(DishTag)