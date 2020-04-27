from django.db import models

# Create your models here.
from notes.models import Note
from users.models import User


class Comment(models.Model):
    """
    uk - person who left comment
    nk - note which was commented
    tk - commentator's text
    dk - when comment was left
    lk - like other persons
    """
    uk = models.ForeignKey(User, verbose_name='uk', on_delete=models.DO_NOTHING)
    nk = models.ForeignKey(Note, verbose_name='nk', on_delete=models.CASCADE)
    tk = models.CharField(max_length=150, verbose_name="tk")
    dk = models.DateTimeField(auto_now_add=True)
    # to do lk!!!

    def __str__(self):
        return str(f"person- {self.uk} |||| text - {self.tk}")
