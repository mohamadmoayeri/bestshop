from django.urls import path

from .views import dashboard,Edit_Profile,change_password

urlpatterns = [
    path("dashboard",dashboard.as_view(),name="dashboard"),

    path("Edit_Profile/<int:pk>",Edit_Profile.as_view(),name="Edit_Profile"),

    path("change_password",change_password.as_view(),name="change_password"),




]