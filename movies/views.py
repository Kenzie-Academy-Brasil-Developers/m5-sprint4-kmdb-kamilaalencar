from functools import partial
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import MovieCustomPermission
from .models import Movie
from .serializers import MovieSerializer

class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MovieCustomPermission]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class MovieViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MovieCustomPermission]
    
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({'message':'Movie not found'})

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({'message':'Movie not found'})

        serializer = MovieSerializer(movie, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
    
    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({'message':'Movie not found'})
        
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
