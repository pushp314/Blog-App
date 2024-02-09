# myblog/blog/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, publish_blog, signup, read_more, edit_blog, delete_blog, blog

urlpatterns = [
    path('', home, name='home'),
    path('publish/', publish_blog, name='publish_blog'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('read_more/<int:blog_id>/', read_more, name='read_more'),
    path('edit_blog/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('blog/', home, name='blog'),
    path('blog/<int:blog_id>/', blog, name='blog'),

]
