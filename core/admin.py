from django.contrib import admin
from core.models import (
    User, UserAdmin
)

admin.site.register(User, UserAdmin)