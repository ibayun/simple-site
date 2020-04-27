from django.shortcuts import render

# Create your views here.
from django.views import View

from .models  import Note


def all_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes_t/based_page.html', context={'notes': notes})
