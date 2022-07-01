from rest_framework.views import APIView, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from .permissions import ReviewCustomPermission
from .models import Review
from .serializers import ReviewSerializer
from movies.models import Movie


class ReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewCustomPermission]

    def post(self, request, movie_id ):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({'message':'Movie not found'}, status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(critic=request.user, movie = movie)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request, movie_id):
        reviews = Review.objects.filter(movie_id=movie_id)
        if not reviews:
            return Response({'message':'Reviews of this movie not found'}, status.HTTP_404_NOT_FOUND)
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def delete(self, request, review_id):
        try:
            review = Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            return Response({'message':'Review not found'}, status.HTTP_404_NOT_FOUND)
        
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AllReviewsView(APIView, PageNumberPagination):
    def get(self, request):
        reviews = Review.objects.all()
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

