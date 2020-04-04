import uuid
from django.db import models
from django.utils.timezone import pytz as tz
from django.contrib.auth.models import AbstractUser

TIMEZONE_CHOICES = zip(tz.all_timezones, tz.all_timezones)


class ActivityPeriods(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Activity Period'
        verbose_name_plural = 'Activity Periods'


class User(AbstractUser):
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


# class UserActivity(models.Model):
#     id = models.SlugField(max_length=250, blank=False, null=False, primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     tz = models.CharField(choices=TIMEZONE_CHOICES, max_length=200, blank=False)
#     activity_periods = models.ManyToManyField(ActivityPeriods)
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.id = str(uuid.uuid4())
#             while UserActivity.objects.filter(id=self.id).count() > 0:
#                 self.id = str(uuid.uuid4())
#         super(UserActivity, self).save(args, kwargs)
#
#     def __str__(self):
#         return self.user.real_name if self.user.real_name else self.user.username
#
#     class Meta:
#         verbose_name = 'User Activity'
#         verbose_name_plural = 'User Activities'


