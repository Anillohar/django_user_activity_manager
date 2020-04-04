# import UUID for generating 16 digit hex string
import uuid

from django.db import models
from django.utils.timezone import pytz as tz

# Django's default user model
from django.contrib.auth.models import AbstractUser

# getting all available timezones from django timezone library
TIMEZONE_CHOICES = zip(tz.all_timezones, tz.all_timezones)


class ActivityPeriods(models.Model):
    """
    These are the periods of activity of a user, start_time denotes the starting time and
    end_time denotes ending time of user session
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Activity Period'
        verbose_name_plural = 'Activity Periods'


class User(AbstractUser):
    """ We have override the django user model and added field slug which represents the unique id of a user
    """
    slug = models.SlugField(max_length=250, blank=False, null=False)
    real_name = models.CharField(max_length=250, blank=False)
    timezone = models.CharField(choices=TIMEZONE_CHOICES, max_length=200, blank=False)
    activity_periods = models.ManyToManyField(ActivityPeriods)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(uuid.uuid4())
            while User.objects.filter(slug=self.slug).count() > 0:
                self.slug = str(uuid.uuid4())
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.real_name if self.real_name else ''
