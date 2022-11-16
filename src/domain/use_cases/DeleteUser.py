from src.domain.repositories.UserRepository import UserRepository


class DeleteUser:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_id: str) -> bool:
        response = self.repository.destroy(user_id)
        return response
