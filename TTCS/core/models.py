from django.db import models
from django.contrib.auth.models import AbstractUser


class OurUser(AbstractUser):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", db_index=True)
    username = models.CharField(max_length=50, unique=True, db_index=True, verbose_name="Никнейм")
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=11, verbose_name="Номер телефона", unique=True)  # Стоит доработать посмотреть если поле шаблона для телефона
    is_customer = models.BooleanField(default=False, verbose_name="Заказчик")
    is_employer = models.BooleanField(default=False, verbose_name="Исполнитель")
    data_joined = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
