from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

CHOICES = [(1,"Social Media"),(2,"E-mail"),(3,"Bank"),(4,"Credit Card"),(5,"Peduli Lindungi"),(6,"Trading"),(7,"E-Commerce")]

class passlist(models.Model):
    user = models.ForeignKey(User,on_delete = CASCADE, null=False)
    appname = models.PositiveSmallIntegerField(choices=CHOICES, default=4, primary_key=True)
    email= models.EmailField(max_length=254)
    username = models.CharField(max_length=250,null =True)
    password = models.CharField(max_length=250,null =False)

    def __str__(self):
        return f'{self.appname} account with username {self.username}' 