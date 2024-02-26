from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    car_name = models.CharField(max_length=100)
    car_desc = models.TextField()
    car_image = models.ImageField(upload_to="carIMG")