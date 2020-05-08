from time import time
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from users.models import User
# Create your models here.


def generate_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Tag(models.Model):
    name_tag = models.CharField(max_length=30)

    def __str__(self):
        return self.name_tag


class Category(models.Model):
    name_category = models.CharField(max_length=10)

    def __str__(self):
        return self.name_category
#  TODO fff

class Note(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', blank=True)
    created_by = models.ForeignKey(User, null=True, verbose_name='user', on_delete=models.CASCADE)
    data_of_create = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    picture = models.ImageField(null=True, blank=True, upload_to='image/', verbose_name='image')

    def get_absolute_url(self):
        return reverse('note_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('note_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('note_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
