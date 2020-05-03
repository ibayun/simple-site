from django.urls import path, re_path
from users import views


urlpatterns = [
    path("accounts/login/", views.login_view, name='login'),
    path("logout/", views.logout_view),
    path("register/", views.register),
]
