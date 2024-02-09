# myblog/myblog/urls.py
from django.contrib import admin
from django.urls import path, include
from blog.views import home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Django authentication URLs
]
