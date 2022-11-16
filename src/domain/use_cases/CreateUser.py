from src.domain.entities.User import User
from src.domain.repositories.UserRepository import UserRepository


class CreateUser:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, user_data: dict) -> User:
        user = User(user_data)
        self._repository.save(user)
        return user
