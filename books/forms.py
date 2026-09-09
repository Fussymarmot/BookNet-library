from django import forms
from .models import Book

from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'cover', 'file']
        labels = {
            'title': 'Название',
            'author': 'Автор',
            'genre': 'Жанр',
            'description': 'Описание',
            'cover': 'Обложка',
            'file': 'Файл',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название...'}),
            'author': forms.TextInput(attrs={'placeholder': 'Введите автора...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите описание книги...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # "- Select an option -"
        self.fields['genre'].empty_label = 'Выберите жанр'
