from httpx import Response
from typing import TypedDict, Optional

from clients.api_client import APIClient

class UpdateRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self)-> Response:
        return self.get("/api/v1/users/me")
    """
    Метод получения текущего пользователя.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
    def get_user_api(self, user_id: str)-> Response:
        return self.get(f"/api/v1/users/{user_id}")
    """
    Метод получения пользователя по идентификатору.
    :param user_id: Идентификатор пользователя.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
    def update_user_api(self, user_id: str, request: UpdateRequestDict) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json= request)
    """
    Метод обновления пользователя по идентификатору.
    :param user_id: Идентификатор пользователя.
    :param request: Словарь с email, lastName, firstName, middleName.
    :return: Ответ от сервера в виде объекта httpx.Response
    """
    def delete_user_api(self, user_id: str)-> Response:
        return self.delete(f"/api/v1/users/{user_id}")
    """
    Метод удаления пользователя по идентификатору.
    :param user_id: Идентификатор пользователя.
    :return: Ответ от сервера в виде объекта httpx.Response
    """