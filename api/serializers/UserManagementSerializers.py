from rest_framework import serializers
from user_management.models import UserActivity, User, ActivityPeriods


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['real_name']


class ActivityPeriodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']

class UserActivitySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.real_name')
    activity_periods = ActivityPeriodsSerializer(many=True)

    class Meta:
        model = UserActivity
        fields = ['id', 'user', 'tz', 'activity_periods']
