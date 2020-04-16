from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=30)
    language = models.CharField(max_length=10)
    date = models.CharField(max_length=15)
    movie_id = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'movies'

class Movie_Info(models.Model):
    movie_info = models.TextField()
    image_name = models.CharField(max_length=50)
    movie = models.OneToOneField(Movies,on_delete=models.CASCADE,related_name= 'movie',db_column='movie_id',to_field='movie_id' )

    class Meta:
        db_table = 'movie_info'

class LoginForm(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    mail = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

class Purchases(models.Model):
    purchesd = models.IntegerField()
    users = models.IntegerField()

