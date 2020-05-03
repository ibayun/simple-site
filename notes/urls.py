from django.urls import path

from notes.views import all_notes, main_page
from users import views


urlpatterns = [
    path(r"notes/", all_notes, name='all_notes'),
    path("", main_page),
    # path("register", views.register),
]