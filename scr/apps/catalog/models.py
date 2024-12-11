from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Good(models.Model):
    title = models.CharField(max_length=100)

    description = models.CharField(max_length=1000)

    date_created = models.DateTimeField(default=datetime.today)

    price = models.FloatField()

    value = models.IntegerField()

    cart = models.ManyToManyField(
        get_user_model(), through='Order', related_name='cart', blank=True
    )

    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    orders = models.IntegerField(default=0)

    have_bought = models.IntegerField(default=0)

    has_seen = models.IntegerField(default=0)

    income = models.FloatField(default=0)


class Order(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    value = models.IntegerField(default=1)
