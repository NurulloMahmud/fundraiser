from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

from .models import CustomUser



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': ('No active account found with the given credentials')
    }

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')  # Use email as username for authentication
        return super().validate(attrs)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        password = data['password']
        print(password)
