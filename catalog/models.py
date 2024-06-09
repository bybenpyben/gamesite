from django.db import models


class Game(models.Model):
    name = models.CharField('Название игры', max_length=100)
    platform = models.CharField('Платформа', max_length=100)
    ocenka = models.TextField('Оценка игры')
    text = models.TextField()
    image = models.ImageField(upload_to='news_images/')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
