from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models


class Good(models.Model):
    title = models.CharField(max_length=100)

    description = models.CharField(max_length=1000)

    date_created = models.DateTimeField(default=datetime.today)

    price = models.FloatField()

    value = models.IntegerField()

    cart = models.ManyToManyField(get_user_model(), related_name='cart', blank=True)

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
