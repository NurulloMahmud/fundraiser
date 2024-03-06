from django.urls import path
from .views import (
    MyTokenObtainPairView, 
    UserRegisterAPIView, 
)

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', UserRegisterAPIView.as_view())
]
