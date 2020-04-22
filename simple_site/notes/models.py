from django.db import models
# Create your models here.

class Tag():
    name_tag = models.CharField(max_length=30)

class Category():
    name_category = models.CharField(max_length=10)


class Note():
    title = models.CharField(max_length=60)
    body = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
