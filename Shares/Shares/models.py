from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Shares(models.Model):
    #user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    ticker = models.CharField(max_length=300)
    buy_price = models.FloatField()
    number_of_shares = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + str(self.buy_price)

    @property
    def total_cost(self):
        return self.buy_price * self.number_of_shares
