from django.core.management.base import BaseCommand, CommandError

from datetime import datetime
from user_management.models import User
from api.serializers.UserManagementSerializers import UserSerializer, ActivityPeriods


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            AutoPopulateDatabase()
        except Exception as e:
            raise CommandError('Something went wrong!!', str(e))
        self.stdout.write(self.style.SUCCESS('Successfully saved dummy data'))


class AutoPopulateDatabase:
    model = User
    serializer = UserSerializer
    _user_dummy_data = (('anillohar987', 'anillohar03@gmail.com', 'anil lohar', 'Asia/Kolkata'),
                        ('vishnupalmquist', 'vishnu@gmail.com', 'vihnu jangid', 'Asia/Kolkata'),
                        ('Joeincornavia09', 'joe@gmail.com', 'joe sharma', 'America/Antigua'))

    def __init__(self):
        if self.model.objects.filter(username='anillohar987').count()==0:
            activity_period = [ActivityPeriods.objects.create(start_time=datetime.utcnow(), end_time=datetime.utcnow()) for i in range(3)]
            for user in self.__auto_populate_database():
                user.activity_periods.set(activity_period)
                user.save()

    def __auto_populate_database(self):
        data = []
        for username, email, realname, timezone in self._user_dummy_data:
            data.append(self._make_user_data(username, email, realname, timezone))
        serializer = self.serializer(data=data, many=True)
        if serializer.is_valid():
            instances = serializer.save()
            return instances
        else:
            print('dummy data not saved, error is: ', str(serializer.errors))
            return []

    def _make_user_data(self, username, email, realname, timezone):
        return dict(username=username, password='jhkdj@kdjvj23', email=email, real_name=realname,
                    timezone=timezone, is_staff=False, is_active=True, is_superuser=False)

