# Generated by Django 3.2.7 on 2021-10-04 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passlist',
            name='appname',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Social Media'), (2, 'E-mail'), (3, 'Bank'), (4, 'Credit Card'), (5, 'Health Account'), (6, 'Trading'), (7, 'E-Commerce'), (8, 'Other')], default=4),
        ),
    ]
