from django.db import models

"""Создание таблиц за счет классов моделей"""
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    """Метод для отображения информации об объекте класса для пользователей"""
    def __str__(self):
        return self.title   #  Возвращение названия самого объекта

    """Метод для переадресации на страницу после редактирования и/или удаления записи"""
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Hовости'