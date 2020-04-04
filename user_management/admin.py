# importing base django admin
from django.contrib import admin

# importing django's default user admin
from django.contrib.auth.admin import UserAdmin as base_user_admin

# for Internationalization
from django.utils.translation import gettext_lazy as _

from user_management.models import User, ActivityPeriods


@admin.register(User)
class UserAdmin(base_user_admin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'real_name')
    fieldsets = (
        (None, {'fields': ('username', 'real_name', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'timezone', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )


admin.site.register(ActivityPeriods)
