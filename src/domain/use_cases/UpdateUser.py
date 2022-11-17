from src.domain.entities.User import User
from src.domain.repositories.UserRepository import UserRepository


class UpdateUser:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, user_id, user_data: dict) -> dict:
        user = self._repository.find_by_id(user_id)

        if user is None:
            return {
                "message": "There is no such user"
            }

        user = User({
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "email": user_data["email"],
            "genre": user_data["genre"],
        }, user_id)

        updated_user = self._repository.update(user)

        return {
            "UpdatedUserData": updated_user
        }
