import uuid
from datetime import datetime


class User:
    def __init__(self, user_data: dict, id: str = None):
        self._id = id if id else str(uuid.uuid4())
        self._user_data = user_data
        self._created_at = datetime.now().isoformat()
        self._updated_at = datetime.now().isoformat()

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._user_data["first_name"]

    @property
    def last_name(self):
        return self._user_data["last_name"]

    @property
    def email(self):
        return self._user_data["email"]

    @property
    def genre(self):
        return self._user_data["genre"]

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def get_user_data(self):
        return self._user_data

