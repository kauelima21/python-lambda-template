from src.domain.repositories.UserRepository import UserRepository


class FindUser:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_id) -> dict:
        response = self.repository.find_by_id(user_id)
        return response
