from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from empl.models import Empl
from task_tracker.models import Task


class TaskTestCase(APITestCase):
    """Тесты для модели задачи."""

    def setUp(self):
        """Предварительная настройка."""
        self.task = Task.objects.create(
            name="Тест задача",
            parent_task=None,
            empl=None,
            deadline="2026-11-25",
            status="started",
        )

    def test_task_create(self):
        """Тест на создание модели."""
        url = reverse("task_tracker:task-create")
        data = {
            "name": "Написать программу",
            "parent_task": None,
            "empl": None,
            "deadline": "2026-11-25",
            "status": "started",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Написать программу")
        self.assertEqual(response.data["parent_task"], None)
        self.assertEqual(response.data["empl"], None)
        self.assertEqual(response.data["deadline"], "2026-11-25")
        self.assertEqual(response.data["status"], "started")
        self.assertEqual(Task.objects.count(), 2)

    def test_task_retrieve(self):
        """Тест на просмотр модели."""
        url = reverse("task_tracker:task-retrieve", args=(self.task.id,))
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.task.name)
        self.assertEqual(data["parent_task"], self.task.parent_task)
        self.assertEqual(data["empl"], self.task.empl)
        self.assertEqual(data["deadline"], self.task.deadline)
        self.assertEqual(data["status"], self.task.status)

    def test_task_update(self):
        """Тест на редактор модели."""
        url = reverse("task_tracker:task-update", args=(self.task.id,))
        response = self.client.patch(url, {"name": "update task"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "update task")

    def test_task_delete(self):
        """Тест на удаление модели."""
        url = reverse("task_tracker:task-delete", args=(self.task.id,))
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_list(self):
        """Тест на просмотр листа моделей."""
        url = reverse("task_tracker:task-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

    def test_important_task_list(self):
        """Тест поиск менее загруженных работников."""
        empl = Empl.objects.create(full_name="Тест работник", post="Тест пост")

        t0 = Task.objects.create(
            name="Тест задача0",
            empl=empl,
            deadline=None,
            status="created",
            parent_task=None,
        )

        t1 = Task.objects.create(
            name="Тест задача",
            empl=empl,
            deadline=None,
            status="started",
            parent_task=t0
        )


        url = reverse("task_tracker:tracker")
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["available_empl"], ["Тест работник"])
