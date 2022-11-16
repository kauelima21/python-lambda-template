from src.domain.repositories.UserRepository import UserRepository


class FindAllUsers:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> dict:
        response = self.repository.find()
        return response
