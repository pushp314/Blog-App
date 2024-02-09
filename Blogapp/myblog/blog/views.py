# myblog/blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Blog, Category
from .forms import BlogForm
from django.urls import reverse






def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

@login_required
def publish_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        form.instance.author = request.user

        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category, created = Category.objects.get_or_create(name=category_name)
            form.instance.category = category

            form.save()

            # Get the URL for redirection using reverse
            redirect_url = reverse('blog')
            return redirect(redirect_url)
    else:
        form = BlogForm()

    return render(request, 'publish_blog.html', {'form': form})




def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})


# myblog/blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after signup
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})



# myblog/blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Blog

def read_more(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'read_more.html', {'blog': blog})



@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category, created = Category.objects.get_or_create(name=category_name)
            form.instance.category = category
            form.save()
            return redirect('blog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog')
    return render(request, 'delete_blog.html', {'blog': blog})



def blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog.html', {'blog': blog,})

