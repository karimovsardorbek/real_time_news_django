from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),       # POST username/password
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]
