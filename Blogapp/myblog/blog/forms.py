# myblog/blog/forms.py
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.Textarea()
    category_name = forms.CharField(max_length=50)  # Add a field for the category name

    class Meta:
        model = Blog
        fields = ['title', 'content', 'category_name']
