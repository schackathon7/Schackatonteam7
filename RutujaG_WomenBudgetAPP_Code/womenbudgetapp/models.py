from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    data_created = models.DateTimeField(auto_now_add=True, null=True)


class GoalSet(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    goaltitle = models.CharField(max_length=300)
    targetamount = models.CharField(max_length=100)
    capitalamount = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    ym = models.CharField(max_length=100)
    savings = models.CharField(max_length=100)


class Wallet(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    walletamount = models.CharField(max_length=100, default='0')


def save_post(sender, instance, **kwargs):
    Wallet.objects.create(user=instance)




# signals
post_save.connect(save_post, sender=User)
