from django.contrib import admin
from django.urls import path, include
from car.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index, name="index"),
    path('delete_car/<id>', delete_car, name="delete_car"),
    path('update_car/<id>', update_car, name="update_car"),
    path("login/", login_page, name="login_page"),
    path("logout_page/", logout_page, name="logout_page"),
    path("register/", register, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)