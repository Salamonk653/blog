from django.db import models

class User(models.Model):

    class Meta():
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    name = models.CharField("Имя", max_length=30)
    email = models.EmailField("Эмейл")

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name
