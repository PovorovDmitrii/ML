import json
from datetime import datetime
from json import JSONEncoder
from typing import TypeVar, Generic, Dict, Optional, Type, List
from pydantic import BaseModel
import os

T = TypeVar('T', bound=BaseModel)

class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class BaseRepository(Generic[T]):
    def __init__(self, file_path: str, model: Type[T]):
        # TODO: Реализуйте инициализацию
        self._file_path = file_path
        self._model = model
        self._data: Dict[int, T] = {}

        self._load()
        

    def _load(self) -> None:
        # TODO: Реализуйте загрузку данных из файла

        if not os.path.exists(self._file_path):
            return
        
        with open(self._file_path, "+r", encoding="utf-8") as f:
            data = json.load(f)

        self._data = {
            int(k): self._model(**v)
            for k, v in data.items()
        }
        

    def _save(self) -> None:
        # TODO: Реализуйте сохранение данных в файл
        data = {
            str(k): v.model_dump(mode="json")
            for k, v in self._data.items()
        }
        with open(self._file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def add(self, item: T) -> T:
        # TODO: Реализуйте добавление элемента
        if item.id in self._data:
            raise ValueError(f"Item with id {item.id} already exists")
        
        self._data[item.id] = item
        self._save()
        return item
    

    def get(self, id_: int) -> Optional[T]:
        # TODO: Реализуйте получение элемента по ID
        return self._data.get(id_)

    def get_all(self) -> List[T]:
        # TODO: Реализуйте получение всех элементов
        return list(self._data.values())

    def update(self, id_: int, **kwargs) -> bool:
        # TODO: Реализуйте обновление элемента
        item = self.get(id_)
        if not item:
            return False
        
        for key, value in kwargs.items():
            setattr(item, key, value)

        self._save
        return True

    def delete(self, id_: int) -> bool:
        # TODO: Реализуйте удаление элемента
        if id_ not in self._data:
            return False
        
        del self._data[id_]

        self._save
        return True
    