from django.db import models


# Create your models here.


class User(models.Model):
    login_user = models.CharField(max_length=30)
    first_name_user = models.CharField(max_length=30)
    last_name_user = models.CharField(max_length=30)
    email_user = models.EmailField(max_length=100)
    data_of_register = models.DateField(auto_now_add=True)
    last_user_visit = models.DateField(auto_now=True)

