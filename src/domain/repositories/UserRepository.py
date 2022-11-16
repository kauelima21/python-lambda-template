from abc import ABC, abstractmethod
from src.domain.entities.User import User


class UserRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save(self, user: User) -> bool:
        pass

    @abstractmethod
    def find(self, count=False) -> dict:
        pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> dict:
        pass

    @abstractmethod
    def update(self, user: User) -> dict:
        pass

    @abstractmethod
    def destroy(self, user_id: str) -> bool:
        pass
