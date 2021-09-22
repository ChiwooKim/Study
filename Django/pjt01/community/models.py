from django.db import models
from django.db.models.fields import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.title
