from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from .permissions import UserCustomPermission
from .models import User
from .serializers import UserSerializer
from .serializers import LoginUserSerializer


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserCustomPermission]
 
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data, status.HTTP_200_OK)

class UserViewDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserCustomPermission]

    def get(self, request, user_id):
        try: 
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'message':'User not found'}, status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


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