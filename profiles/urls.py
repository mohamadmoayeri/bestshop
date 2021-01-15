from django.urls import path

from .views import dashboard,Edit_Profile,change_password,change_password_done,delete_avatar,upload_ads,delete_account

urlpatterns = [
    path("dashboard",dashboard.as_view(),name="dashboard"),

    path("Edit_Profile/<int:pk>",Edit_Profile.as_view(),name="Edit_Profile"),

    path("change_password",change_password.as_view(),name="change_password"),

    path("change_password_done20212",change_password_done.as_view(),name="change_password_done"),

    path("delete_avatar/<int:pk>",delete_avatar,name="delete_avatar"),

    path("delete_account",delete_account,name="delete_account"),

    path("upload-ads/<slug:user>",upload_ads.as_view(),name="upload-ads"),

    






]