from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    direction = models.TextField(blank=True)
    protein = models.CharField(max_length=50)
    carb = models.CharField(max_length=50)
    veggie = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Favorites(models.Model):
    user_id = models.ForeignKey(User, related_name='user_favorites', on_delete=models.CASCADE)
    recipe_id = models.IntegerField()
