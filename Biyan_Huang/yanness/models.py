from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


# class ToDoL(models.Model):
#     title = models.CharField(max_length=300, default='todo_list title')
#
#     def __str__(self):
#         return self.title
#
#
# class Item(models.Model):
#     todoList = models.ForeignKey(ToDoL, on_delete=models.CASCADE)
#     description = models.CharField(max_length=400, default='item description')
#     complete = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.description


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField(null=True)
    rating = models.FloatField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    last_updated = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_by = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=100000)
    rating = models.FloatField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return f"{self.user.username}: {self.review}"
