from django.urls import path
from .views import (
    MyTokenObtainPairView, 
    TokenRefreshView,
    UserRegisterAPIView, 
)

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', UserRegisterAPIView.as_view())
]
