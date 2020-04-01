from django.db import models
from django.utils.timezone import pytz as tz
from django.contrib.auth.models import AbstractUser

TIMEZONE_CHOICES = zip(tz.all_timezones, tz.all_timezones)

class User(AbstractUser):
    real_name = models.CharField(max_length=250, blank=False)


class ActivityPeriods(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Activity Period'
        verbose_name_plural = 'Activity Periods'


class UserActivity(models.Model):
    id = models.SlugField(max_length=250, blank=False, null=False, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tz = models.CharField(choices=TIMEZONE_CHOICES, max_length=200, blank=False)
    activity_periods = models.ManyToManyField(ActivityPeriods)

    class Meta:
        verbose_name = 'User Activity'
        verbose_name_plural = 'User Activities'

    def __str__(self):
        return self.user.real_name if self.user.real_name else self.user.username


