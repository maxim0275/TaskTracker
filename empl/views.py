from django.db.models import Count, Q
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from empl.models import Empl
from empl.serializers import EmplSerializer, EmplTaskSerializer
from task_tracker.models import Task


class EmplCreateAPIView(CreateAPIView):
    """Создание работника."""

    serializer_class = EmplSerializer


class EmplListAPIView(ListAPIView):
    """Просмотр листа работников."""

    serializer_class = EmplSerializer
    queryset = Empl.objects.all()


class EmplRetrieveAPIView(RetrieveAPIView):
    """Просмотр работника."""

    serializer_class = EmplSerializer
    queryset = Empl.objects.all()


class EmplUpdateAPIView(UpdateAPIView):
    """Редактирование работника."""

    serializer_class = EmplSerializer
    queryset = Empl.objects.all()


class EmplDestroyAPIView(DestroyAPIView):
    """Удаление работника."""

    queryset = Empl.objects.all()


class EmplTaskListAPIView(ListAPIView):
    """Просмотр для подсчета активных задач работника."""

    queryset = Empl.objects.all()
    serializer_class = EmplTaskSerializer

    def get_queryset(self):
        return (
            Empl.objects.annotate(
                active_tasks_count=Count("tasks", filter=Q(tasks__status="started"))
                )
            .filter(active_tasks_count__gt=0)
            .order_by("-active_tasks_count")
        )


class EmployeeLessLoadedListAPIView(ListAPIView):
    serializer_class = EmplTaskSerializer

    def get_queryset(self):
        qs = Empl.objects.annotate(task_count=Count("tasks"))
        min_count = qs.orderby("task_count").values_list("task_count").first()

        return (
            qs.filter(
                Q(task_count=min_count)
                |
                Q(task_count__gte=min_count + 2) & Q(
                    tasks__in=Task.objects.filter(parent_task__isnull=False).values("parent_task")))
        )

