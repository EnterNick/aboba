from django.contrib.auth import get_user_model
from django.db import models


class FeedbackTicket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    email = models.CharField(max_length=100)

    text = models.CharField(max_length=1000)

    name = models.CharField(max_length=100)

    tel = models.CharField(max_length=100)
