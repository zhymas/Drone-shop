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
    POLAND = 'Poland'
    UKRAINE = 'Ukraine'

    COUNTRY = (
        (POLAND, 'Poland'),
        (UKRAINE, 'Ukraine')
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE, related_name='drone_order')
    date = models.DateTimeField(auto_now_add=True)
    coutry = models.CharField(max_length=255, choices=COUNTRY, default=UKRAINE)
    city = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    number_of_phone = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.drone
    

