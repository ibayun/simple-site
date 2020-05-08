from django.urls import path

from notes.views import all_notes, main_page, note_detail
from users import views


urlpatterns = [
    path(r"notes/", all_notes, name='all_notes'),
    # path(r"notes/<?slug>", note_detail, name="note_detail"),
    path("", main_page),
    # path("register", views.register),
]