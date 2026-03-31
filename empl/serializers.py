from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from empl.models import Empl
from task_tracker.serializers import TaskSerializer


class EmplSerializer(ModelSerializer):
    """Сериалайзер модели работника."""

    class Meta:
        model = Empl
        fields = "__all__"


class EmplTaskSerializer(TaskSerializer):
    """Сериалайзер модели для подсчета активных задач работника."""

    tasks = TaskSerializer(many=True, read_only=True)
    active_tasks_count = SerializerMethodField()

    class Meta:
        model = Empl
        fields = (
            "id",
            "full_name",
            "post",
            "tasks",
            "active_tasks_count",
        )

    def get_active_tasks_count(self, obj):
        return obj.tasks.filter(status="start").count()
