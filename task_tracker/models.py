from django.db import models

from empl.models import Empl

NULLABLE = {"blank": True, "null": True}

TASK_STATUS = [
    ("start", "start"),
    ("finish", "finish"),
]

FATHER_TASK = [("father", "father"), ("other", "other")]


class Task(models.Model):
    """Создаем модель задачи."""

    name = models.CharField(
        max_length=100, verbose_name="Name", help_text="Введите наименование задачи"
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="other",
        help_text="Введите родительскую задачу",
        **NULLABLE
    )
    empl = models.ForeignKey(
        Empl,
        verbose_name="Исполнитель",
        related_name="tasks",
        on_delete=models.CASCADE,
        help_text="Введите исполнителя",
        **NULLABLE
    )
    deadline = models.DateField(
        verbose_name="Срок исполнения", help_text="Введите срок исполнения", **NULLABLE
    )
    status = models.CharField(
        choices=TASK_STATUS,
        default=TASK_STATUS[0][0],
        verbose_name="Статус",
        help_text="Введите статус",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
