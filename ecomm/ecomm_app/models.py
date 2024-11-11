from django.db import models

class Msg(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    message=models.CharField(max_length=150)
