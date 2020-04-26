from django.db import models
from users.models import User
# Create your models here.


class Tag(models.Model):
    name_tag = models.CharField(max_length=30)

    def __str__(self):
        return self.name_tag


class Category(models.Model):
    name_category = models.CharField(max_length=10)

    def __str__(self):
        return self.name_category


class Note(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag')
    created_by = models.ForeignKey(User, null=True, verbose_name='user', on_delete=models.CASCADE)
    data_of_create = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


