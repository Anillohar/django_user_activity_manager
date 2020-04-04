from rest_framework.routers import DefaultRouter
from api.views import MembersListViewset

router = DefaultRouter()
router.register(r'get-members-list', MembersListViewset, basename='get_members_list')
urlpatterns = router.urls
