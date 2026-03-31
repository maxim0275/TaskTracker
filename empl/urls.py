from django.urls import path

from empl.apps import EmplConfig
from empl.views import (EmplCreateAPIView, EmplDestroyAPIView, EmplListAPIView,
                        EmplRetrieveAPIView, EmplTaskListAPIView,
                        EmplUpdateAPIView)

app_name = EmplConfig.name

urlpatterns = [
    path("create/", EmplCreateAPIView.as_view(), name="empl-create"),
    path("list/", EmplListAPIView.as_view(), name="empl-list"),
    path("<int:pk>/", EmplRetrieveAPIView.as_view(), name="empl-retrieve"),
    path("update/<int:pk>/", EmplUpdateAPIView.as_view(), name="empl-update"),
    path("delete/<int:pk>/", EmplDestroyAPIView.as_view(), name="empl-delete"),
    path("empl_task/", EmplTaskListAPIView.as_view(), name="empl-task"),
]
