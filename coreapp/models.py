
from django.db import models

# Create your models here.
from accounts.models import User
from django.utils import timezone


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    weigh_word = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class MyFittness(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    weigh_photo = models.ImageField(upload_to='weight_photo', blank=True, null=True)
    body_photo = models.ImageField(upload_to='body_photo', blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.entry_date)
