from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Drone(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.DecimalField(max_digits=3, decimal_places=0)
    image = models.ImageField(upload_to='drone_img/')
    specifications = models.TextField()
    manufacturer = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE, related_name='drone_order')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.drone
    

