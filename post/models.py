from django.db import models

from user.models import User


class Post(models.Model):

    class Meta():
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['created']

    user = models.ForeignKey(User)
    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст статьи")
    image = models.ImageField("Изоброжение", upload_to='post/', blank=True)
    created = models.DateTimeField("Создан", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this_record = Post.objects.get(id=self.id)

            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(Post, self).save(*args, **kwargs)


class HashTag(models.Model):

    class Meta():
        db_table = 'Tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField("Имя", max_length=50, unique=True)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
