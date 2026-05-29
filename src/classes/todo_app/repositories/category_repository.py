from src.classes.todo_app.models.category import Category
from src.classes.todo_app.repositories.base_repository import BaseRepository
from typing import Optional

class CategoryRepository(BaseRepository[Category]):
    def __init__(self, file_path: str):
        # TODO: Реализуйте инициализацию
        super().__init__(file_path, Category)
        

    def get_by_name(self, name: str) -> Optional[Category]:
        # TODO: Реализуйте поиск по имени
        for category in self._data.values():
            if category.name.lower() == name.lower():
                return category
        
        return None
        