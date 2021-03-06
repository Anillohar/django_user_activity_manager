from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from user_management.models import User
from api.serializers.UserManagementSerializers import UserSerializer


class MembersListViewset(ViewSet):
    """To get all present users details from database"""
    model = User
    serializer = UserSerializer
    fields = ['id', 'real_name', 'tz', 'activity_periods']

    def list(self, request):
        try:
            user_activities = self.serializer(self.model.objects.all(), many=True, context={'fields':self.fields})
            return Response({'ok': True, 'members': user_activities.data})
        except Exception as e:
            print(e)
            return Response({'ok': False, 'message': str(e)})