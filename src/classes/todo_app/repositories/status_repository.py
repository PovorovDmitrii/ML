from src.classes.todo_app.models.status import Status
from src.classes.todo_app.repositories.base_repository import BaseRepository

class StatusRepository(BaseRepository[Status]):
    def __init__(self, file_path: str):
        # TODO: Реализуйте инициализацию
        super().__init__(file_path, Status)

        if not self._data:
            self._init_default_statuses()
        

    def _init_default_statuses(self) -> None:
        # TODO: Реализуйте инициализацию статусов по умолчанию
        statuses = [
            Status(id=1, name="В ожидании"),
            Status(id=2, name="В работе"),
            Status(id=3, name="Завершено")
        ]
        for status in statuses:
            self.add(status)

    def is_valid_status(self, status_id: int) -> bool:
        # TODO: Реализуйте проверку валидности статуса
        return status_id in self._data