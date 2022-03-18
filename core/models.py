from django.db import models


class Task(models.Model):
    """Класс для задач"""
    performer = models.ForeignKey('Performer', on_delete=models.SET_NULL)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    title = models.CharField(max_length=150, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи", blank=True, null=True)
    creation_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, db_index=True)
    # execution_time - время выполнения не знаю надо ли добавлять

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        order_by = ('-creation_date',)


# Вообще все пользователи не от моделей должны наследоваться но не суть
class Performer(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    performer_rating = models.ForeignKey('PerformerRating', on_delete=models.SET_NULL)
    tasks = models.ForeignKey('Tasks', on_delete=models.PROTECT)
    registration_date = models.DateField(auto_now=True, verbose_name="Дата регистрации")


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    customer_rating = models.ForeignKey('CustomerRating', on_delete=models.SET_NULL)
    tasks = models.ForeignKey('Tasks', on_delete=models.PROTECT)
    registration_date = models.DateField(auto_now=True, verbose_name="Дата регистрации")

