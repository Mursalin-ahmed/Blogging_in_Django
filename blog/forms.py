# blog/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # Connects to the Article model
        fields = ['title', 'content']  # Specifies the fields to include in the form
        labels = {
            'title': 'Article Title',  # Adds a label for the 'title' field
            'content': 'Article Content',  # Adds a label for the 'content' field
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter article title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your article content here...'}),
        }
