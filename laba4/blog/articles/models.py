from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    """
    Модель статьи для блога.
    """
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        """Возвращает строковое представление статьи (для админки)."""
        return f"{self.author.username}: {self.title}"

    def get_excerpt(self):
        """Возвращает краткое содержание статьи (первые 140 символов)."""
        if len(self.text) > 140:
            return self.text[:140] + "..."
        return self.text

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_date']  # Новые статьи сверху