from django.db import models
from django.contrib.auth.models import AbstractUser


CHOICES = [
    (1, "Ожидает исполнителя"),
    (2, "В работе"),
    (3, "Заказ выполнен"),
]


class CustomUser(AbstractUser):
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


class SequenceCustomers(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    task_id = models.ForeignKey('Task', on_delete=models.PROTECT)


class SequenceEmployers(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    task_id = models.ForeignKey('Task', on_delete=models.PROTECT)


class Task(models.Model):
    """Класс для задач"""
    customer = models.ForeignKey('SequenceCustomers', on_delete=models.PROTECT)
    employer = models.ForeignKey('SequenceEmployers', on_delete=models.PROTECT)
    title = models.CharField(max_length=150, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, db_index=True)
    date_executed = models.DateTimeField(verbose_name='Дата окончания')
    status = models.CharField(max_length=1, choices=CHOICES, verbose_name="Статус")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class CustomerStat(models.Model):
    """Класс для статистики заказчика"""
    total_rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Общий рейтинг", default=0)
    clear_requirements = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Правильное составление требований", default=0)
    amiability = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Приятность в общении", default=0)
    fair_pay = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Справедливая оплата", default=0)
    correct_timing = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Корректные сроки", default=0)


class EmployerStat(models.Model):
    """Класс для статистики исполнителя"""
    total_rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Общий рейтинг", default=0)
    quality_of_work = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Качество работы", default=0)
    working_speed = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Скорость работы", default=0)
    amiability = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Приятность в общении", default=0)
    team_work = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Работа в команде", default=0)