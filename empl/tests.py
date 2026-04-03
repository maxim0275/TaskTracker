from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from empl.models import Empl
from task_tracker.models import Task


class emplTestCase(APITestCase):
    """Тесты для модели работника."""

    def setUp(self):
        """Предварительная настройка."""
        self.empl = Empl.objects.create(full_name="Тест имя", post="Тест должность")

    def test_empl_create(self):
        """Тест на создание модели."""
        url = reverse("empl:empl-create")
        data = {"full_name": "Петров Иван", "post": "developer"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["full_name"], "Петров Иван")
        self.assertEqual(response.data["post"], "developer")
        self.assertEqual(Empl.objects.count(), 2)

    def test_empl_retrieve(self):
        """Тест на просмотр модели."""
        url = reverse("empl:empl-retrieve", args=(self.empl.id,))
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["full_name"], self.empl.full_name)
        self.assertEqual(data["post"], self.empl.post)

    def test_empl_update(self):
        """Тест на редактор модели."""
        url = reverse("empl:empl-update", args=(self.empl.id,))
        response = self.client.patch(
            url, data={"full_name": "updated name", "post": "update developer"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["full_name"], "updated name")
        self.assertEqual(response.data["post"], "update developer")

    def test_empl_delete(self):
        """Тест на удаление модели."""
        url = reverse("empl:empl-delete", args=(self.empl.id,))
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Empl.objects.count(), 0)

    def test_empl_list(self):
        """Тест на просмотр листа моделей."""
        url = reverse("empl:empl-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Empl.objects.count(), 1)

    def test_empl_task_list(self):
        """Тест для подсчета активных задач работника"""
        Task.objects.create(
            name="Test task",
            empl=self.empl,
            deadline=None,
            status="started",
            parent_task=None,
        )
        url = reverse("empl:empl-task")
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["active_tasks_count"], 1)
