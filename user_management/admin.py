from django.contrib import admin
from user_management.models import User, UserActivity, ActivityPeriods
from django.contrib.auth.admin import UserAdmin as base_user_admin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(base_user_admin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'real_name')
    fieldsets = (
        (None, {'fields': ('username', 'real_name', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'real_name', 'password1', 'password2'),
        }),
    )

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    fields = ['user', 'tz', 'activity_periods']
    class Meta:
        model = UserActivity


admin.site.register(ActivityPeriods)
