from rest_framework import permissions
from reviews.models import Review

class ReviewCustomPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    
    if request.method == 'DELETE':
      review = Review.objects.get(id=view.kwargs.get('review_id', None))
      print(review)
      if review.critic == request.user or request.user.is_superuser:
        return True
      else:
        return False

    if request.method in permissions.SAFE_METHODS:
        return True
    return (
      request.user.is_authenticated
    )