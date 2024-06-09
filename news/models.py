from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=150)
    text = models.TextField('Статья')
    image = models.ImageField(upload_to='news_images/')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
