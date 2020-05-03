from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views import View

from comments.models import Comment
from .models import Note


@login_required(redirect_field_name="u")
def all_notes(request):

    notes = Note.objects.all()
    comments = Comment.objects.all()
    return render(request, 'notes_t/all_notes.html',
                  context={
                      'notes': notes,
                      'comments': comments,
                  })


def main_page(request):
    return render(request, 'notes_t/main_page.html')