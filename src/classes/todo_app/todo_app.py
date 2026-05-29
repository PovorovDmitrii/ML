import os
from datetime import datetime
from typing import List, Optional
from pathlib import Path

from src.classes.todo_app.models.task import Task
from src.classes.todo_app.models.category import Category
from src.classes.todo_app.models.status import Status
from src.classes.todo_app.repositories.task_repository import TaskRepository
from src.classes.todo_app.repositories.category_repository import CategoryRepository
from src.classes.todo_app.repositories.status_repository import StatusRepository


class TodoApp:
    """
    Основной класс приложения для управления задачами.
    Предоставляет доступ к репозиториям и методы с бизнес-логикой.
    """
    
    def __init__(self, data_dir: str):
        """
        Инициализация приложения.
        
        Args:
            data_dir: Путь к директории с JSON файлами данных
        """
        # TODO: Реализуйте инициализацию
        # Создайте репозитории и сохраните их как атрибуты:
        # self.task_repo = TaskRepository(...)
        # self.category_repo = CategoryRepository(...)
        # self.status_repo = StatusRepository(...)
        os.makedirs(data_dir, exist_ok=True)

        self.task_repo = TaskRepository(
            os.path.join(data_dir, "tasks.json")
        )

        self.category_repo = CategoryRepository(
            os.path.join(data_dir, "categories.json")
        )

        self.status_repo = StatusRepository(
            os.path.join(data_dir, "statuses.json")
        )
    
    def add_task(self, title: str, category_id: int, status_id: int, **kwargs) -> Task:
        """
        Добавить новую задачу с проверкой существования категории и статуса.
        
        Args:
            title: Заголовок задачи
            category_id: ID категории
            status_id: ID статуса
            **kwargs: Дополнительные параметры (description, deadline, repeat_every)
            
        Returns:
            Созданная задача
            
        Raises:
            ValueError: Если категория или статус не существуют
        """
        # TODO: Реализуйте добавление задачи
        # 1. Проверьте существование категории и статуса
        # 2. Получите следующий ID для задачи
        # 3. Создайте задачу и добавьте её через репозиторий
        if not self.category_repo.get(category_id):
            raise ValueError("Категории не сущестует")

        if not self.status_repo.is_valid_status(status_id):
            raise ValueError("Статуса не сущестует")

        new_id = (
            max(self.task_repo.items.keys(), default=0) + 1
        )

        task = Task(
            id=new_id,
            title=title,
            category_id=category_id,
            status_id=status_id,
            **kwargs
        )

        return self.task_repo.add(task)
    
    def mark_task_done(self, task_id: int) -> bool:
        """
        Отметить задачу как выполненную.
        
        Args:
            task_id: ID задачи
            
        Returns:
            True, если задача обновлена, False если не найдена
        """
        # TODO: Реализуйте отметку задачи как выполненной
        task = self.task_repo.get(task_id)

        if not task:
            return False

        return self.task_repo.update(
            task_id,
            is_done=True
        )
    
    def get_overdue_tasks(self) -> List[Task]:
        """
        Получить просроченные задачи.
        
        Returns:
            Список задач с истекшим дедлайном
        """
        # TODO: Реализуйте получение просроченных задач
        # Получите все задачи и отфильтруйте те, у которых:
        # - есть дедлайн
        # - дедлайн истек (меньше текущего времени)
        # - задача не выполнена
        now = datetime.now()

        return [
            task for task in self.task_repo.get_all()
            if (
                task.deadline
                and task.deadline < now
                and not task.is_done
            )
        ]


def load_sample_data(app: TodoApp) -> None:
    """
    Загрузить примерные данные в приложение.
    
    Args:
        app: Экземпляр TodoApp
    """
    # TODO: Реализуйте загрузку примерных данных
    # Добавьте категории, статусы и примерные задачи
    categories = [
        Category(id=1, name="Работа"),
        Category(id=2, name="Личное"),
        Category(id=3, name="Учеба")
    ]

    for category in categories:
        app.category_repo.add(category)

    app.add_task(
        title="Изучить Python",
        category_id=3,
        status_id=1,
        description="Изучить основы Python"
    )

    app.add_task(
        title="Купить продукты",
        category_id=2,
        status_id=2,
        description="Молоко, хлеб, яйца"
    )



def print_task(task: Task) -> None:
    """
    Вывести информацию о задаче.
    
    Args:
        task: Задача для вывода
    """
    # TODO: Реализуйте вывод информации о задаче
    print(f"""
    ID: {task.id}
    Название: {task.title}
    Описание: {task.description}
    Категория ID: {task.category_id}
    Статус ID: {task.status_id}
    Выполнена: {task.is_done}
    Дедлайн: {task.deadline}
    Создана: {task.created_at}
    """)


def print_tasks(tasks: List[Task]) -> None:
    """
    Вывести список задач.
    
    Args:
        tasks: Список задач для вывода
    """
    # TODO: Реализуйте вывод списка задач
    for task in tasks:
        print_task(task)


if __name__ == "__main__":
    # Пример использования
    app = TodoApp("src/classes/todo_app/data")
    
    # Загружаем примерные данные
    load_sample_data(app)
    
    print("=== Все задачи ===")
    # Теперь работаем с репозиторием напрямую
    all_tasks = app.task_repo.get_all()
    print_tasks(all_tasks)
    
    print("\n=== Задачи по категории 'Учеба' ===")
    study_tasks = app.task_repo.get_by_category(3)
    print_tasks(study_tasks)
    
    print("\n=== Просроченные задачи ===")
    overdue_tasks = app.get_overdue_tasks()
    print_tasks(overdue_tasks)
    
    # Добавляем новую задачу через высокоуровневый API
    print("\n=== Добавляем новую задачу ===")
    new_task = app.add_task(
        title="Новая задача",
        category_id=1,
        status_id=1,
        description="Это новая задача для демонстрации"
    )
    print_task(new_task) 