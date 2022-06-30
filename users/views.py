from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from .serializers import LoginUserSerializer


class UserView(APIView):
 
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password']
        )
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status.HTTP_200_OK)
        
        return Response(
            {'detail':'invalid email or password'}, status.HTTP_401_UNAUTHORIZED
            )