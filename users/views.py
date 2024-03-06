from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        mobile = request.POST.get('mobile')

        if CustomUser.objects.filter(email=email).exists():
            context = {
                "success": False,
                "message": "This email already exists"
            }

            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if not password == password_confirm:
            context = {
                "success": False,
                "message": "Passwords don't match"
            }

            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            CustomUser.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                mobile=mobile
            )

            context = {
                "success": True,
                "message": "User has been registered successfully"
            }

            return Response(context, status=status.HTTP_201_CREATED)
        except:
            context = {
                "success": False,
                "message": "Missing required fields"
            }

            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
