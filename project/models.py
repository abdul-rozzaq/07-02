from django.db import models


class Food(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=128)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def total_price(self) -> int:
        return self.count * self.food.price
