from django.contrib import admin
from user_management.models import User, UserActivity, ActivityPeriods
from django.contrib.auth.admin import UserAdmin as base_user_admin


@admin.register(User)
class UserAdmin(base_user_admin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'real_name')
    fieldsets = base_user_admin.fieldsets + (
            (None, {'fields': ('real_name',)}),
        )

admin.site.register(UserActivity)
admin.site.register(ActivityPeriods)
