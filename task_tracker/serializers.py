from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from empl.models import Empl
from task_tracker.models import Task
from task_tracker.validators import NameValidator


class TaskSerializer(ModelSerializer):
    """Сериалайзер модели задачи."""

    class Meta:
        model = Task
        fields = "__all__"
        validators = [
            NameValidator(field="name"),
            UniqueTogetherValidator(fields=["name"], queryset=Task.objects.all()),
        ]


class MainTaskSerializer(ModelSerializer):
    """Сериалайзер для поиска работников с наименьшей загрузкой."""

    tasks = TaskSerializer(source="other", many=True)
    available_empl = SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_available_empl(self, task):
        empl = Empl.objects.all()
        emp_data = {}
        for emp in empl:
            list_task = emp.tasks.filter(status="start")
            emp_data[emp.pk] = len(list_task)
        min_count = min(emp_data.values())
        available_empl = [
            emp.full_name for emp in empl if emp_data[emp.pk] == min_count
        ]
        for emp in empl:
            tasks = Task.objects.filter(parent_task=task.id)
            for t in tasks:
                if t.empl == emp and emp.full_name not in available_empl:
                    available_empl.append(emp.full_name)
        return available_empl
