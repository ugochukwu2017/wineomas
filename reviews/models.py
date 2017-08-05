from django.db import models

# Create your models here.
from django.db import models
import numpy as np


class Wine(models.Model):
    name = models.CharField(max_length=200)

    def rating_average(self):
        reviews = Review.objects.filter(wine=self)
        review_rating = [review.rating for review in reviews]
        review_sum = sum(review_rating)
        average_review = review_sum/len(review_rating)
        return average_review

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
