from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializers.UserManagementSerializers import UserActivitySerializer
from user_management.models import UserActivity


class MembersListViewset(ViewSet):

    def list(self, request):
        try:
            user_activities = UserActivitySerializer(UserActivity.objects.all(), many=True)
            return Response({'ok':True, 'members':user_activities.data})
        except Exception as e:
            return Response({'ok':False, 'message':str(e)})