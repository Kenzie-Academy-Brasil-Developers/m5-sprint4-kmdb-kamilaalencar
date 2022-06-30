from django.db import models

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50)
    movies = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='reviews')
    users = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reviews')

