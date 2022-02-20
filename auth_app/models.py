from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user=models.CharField(max_length=300,null=True)
    picture=models.IntegerField(null=False)
    phone=models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.phone

    class Meta:
        db_table='Employee'