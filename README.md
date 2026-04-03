# Система контроля задач работников.

Приложение представляеи собой систему контроля задач работников. 
Позволяет вести список работников, создавать и распределять задачи между работниками, контролировать сроки выполнения, выводить информацию о загрузке работников задачами.

## Система разработана с использованием 
  - фреймворка с открытым исходным кодом Django;
  - свободной объектно-реляционная системы управления базами данных (СУБД) Postgres;
  - библиотеки Django REST Framework;
  - авторизации с помощью пакета Simple JWT фреймворка Django REST;
  - библиотеки drf‑yasg для автоматической генерации документации API.


## Реализовано
 - ведение пользователей, работников, задач с использованием CRUD операций из библиотеки rest_framework.generics;
 - специальные API, позволяющие получать информацию о загруженности работников и о важных задачах;
 

### Для запуска проекта локально потребуется:
  - установить Git и Docker;
  - клонировать репозиторий;
  - создать и заполнить файл .env нужными данными;
  - запустить терминал и выполнить команды: docker-compose build , docker-compose up;
  - для доступа к администрированию выполнить команду: docker-compose exec app python manage.py csu (пользователь с административными правами email="admin@gmail.com" password="789654").


### CRUD URL

    [POST] http://localhost:8000/empl/create/ - Создание юзера.

    [POST] http://localhost:8000/users/token/ - Создание JWT токена.

    [GET] http://localhost:8000/empl/list/ - Просмотр листа работников.

    [GET] http://localhost:8000/empl/{id}/ - Просмотр работника.

    [POST] http://localhost:8000/empl/create/ - Создание работника.

    [PATCH] http://localhost:8000/empl/update/{id}/ - Редактирование работника.

    [DELETE] http://localhost:8000/empl/delete/{id}/ - Удаление работника.

    [GET] http://localhost:8000/task_tracker/list/ - Просмотр листа задач.

    [GET] http://localhost:8000/task_tracker/{id}/ - Просмотр задачи.

    [POST] http://localhost:8000/task_tracker/create/ - Создание задачи.

    [PATCH] http://localhost:8000/task_tracker/update/{id}/ - Редактирование задачи.

    [DELETE] http://localhost:8000/task_tracker/delete/{id}/ - Удаление задачи.

    http://127.0.0.1:8000/swagger/, http://127.0.0.1:8000/redoc/ - документация для API

### Специализированные URL

    [GET] http://localhost:8000/empl/empl_task/ - Просмотр для подсчета активных задач работника.
    [GET] http://localhost:8000/task_tracker/tracker/ - Поиск менее загруженных работников.

### Полная документация 
http://localhost:8000/redoc/ или http://localhost:8000/swagger/