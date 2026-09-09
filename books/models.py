from django.conf import settings
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)  # название книги
    author = models.CharField(max_length=100)  # автор
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  # жанр
    description = models.TextField()  # описание книги
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # обложка книги
    file = models.FileField(upload_to='book_files/', blank=True, null=True)  # файл книги для скачивания
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books',
    )  # кто добавил книгу
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
