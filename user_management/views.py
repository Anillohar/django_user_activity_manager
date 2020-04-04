from datetime import datetime
from user_management.models import ActivityPeriods
from django.contrib.auth.views import LoginView as base_login_view, LogoutView as base_logout_view


class LoginView(base_login_view):
    template_name = 'admin/login.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if self.request.user.is_authenticated:
            activity_period = ActivityPeriods.objects.create(start_time=datetime.now())
            self.request.user.activity_periods.add(activity_period)
            self.request.user.save()
        return response


class LogoutView(base_logout_view):

    def dispatch(self, request, *args, **kwargs):
        user = getattr(request, 'user', None)
        if getattr(user, 'is_authenticated', True):
            last_activity = self.request.user.activity_periods.last()
            last_activity.end_time = datetime.now()
            last_activity.save()
        return super(LogoutView, self).dispatch(request, args, kwargs)


