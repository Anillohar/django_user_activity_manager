from rest_framework import serializers
from user_management.models import User, ActivityPeriods


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)

        if 'context' in kwargs:
            if 'fields' in kwargs['context']:
                    included = set(kwargs['context']['fields'])
                    existing = set(self.fields.keys())
                    for extra_field in existing - included:
                        self.fields.pop(extra_field)

    id = serializers.CharField(source='slug', read_only=True)
    tz = serializers.CharField(source='timezone', read_only=True)
    activity_periods = ActivityPeriodsSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'real_name', 'timezone', 'tz',
                  'activity_periods', 'is_active', 'is_staff', 'is_superuser']
        write_only_fields = ('username', 'password', 'email', 'timezone', 'is_active', 'is_staff', 'is_superuser')

    def create(self, validated_data):
        password = validated_data['password']
        instance = super(UserSerializer, self).create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance
