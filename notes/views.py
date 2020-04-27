from django.shortcuts import render

# Create your views here.
from django.views import View

from comments.models import Comment
from .models import Note


def all_notes(request):
    notes = Note.objects.all()
    comments = Comment.objects.all()
    return render(request, 'notes_t/based_page.html',
                  context={
                      'notes': notes,
                      'comments': comments,
                  })
