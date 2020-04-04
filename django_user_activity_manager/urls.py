from django.contrib import admin
from django.urls import path, include
from user_management.views import LoginView, LogoutView

urlpatterns = [
    path('admin/login/', LoginView.as_view(), name='login'),
    path('admin/logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]
