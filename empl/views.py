from django.db.models import Count, Q
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from empl.models import Empl
from empl.serializers import EmplSerializer, EmplTaskSerializer


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
                active_tasks_count=Count("tasks", filter=Q(tasks__status="start"))
            )
            .filter(active_tasks_count__gt=0)
            .order_by("-active_tasks_count")
        )
