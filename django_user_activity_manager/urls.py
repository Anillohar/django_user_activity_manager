from django.contrib import admin
from django.urls import path, include
from user_management.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', admin.site.urls),
    path('api/v1/', include('api.urls'))
]
