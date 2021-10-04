from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

CHOICES = [(1,"Social Media"),(2,"E-mail"),(3,"Bank"),(4,"Credit Card"),(5,"Health Account"),(6,"Trading"),(7,"E-Commerce"),(8,"Other")]

class passlist(models.Model):
    account_type = models.PositiveSmallIntegerField(choices=CHOICES, default=4)
    email= models.EmailField(max_length=254, null=False)
    application_name = models.CharField(max_length=250, null=True)
    username = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=250, null=False)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f'{self.application_name} account with username {self.username}' 