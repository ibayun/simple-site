from django.urls import path
from users import views


urlpatterns = [
    path("account/login", views.login_view),
    path("logout/", views.logout_view),
    path("register", views.register),
]