from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from login_app import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.home, name='home'),
    path('login/', login_views.custom_login, name='login'),
    path('logout/', login_views.custom_logout, name='logout'),
    path('dashboard/', login_views.dashboard, name='dashboard'),
    path('register/', login_views.register, name='register'),
]