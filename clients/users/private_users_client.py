from httpx import Response
from typing import TypedDict, Optional

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

from clients.users.users_schema import UpdateRequestSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    """
    Метод получения текущего пользователя.
    :return: Ответ от сервера в виде объекта httpx.Response
    """

    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    """
    Метод получения пользователя по идентификатору.
    :param user_id: Идентификатор пользователя.
    :return: Ответ от сервера в виде объекта httpx.Response
    """

    def update_user_api(self, user_id: str, request: UpdateRequestSchema) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    """
    Метод обновления пользователя по идентификатору.
    :param user_id: Идентификатор пользователя. 
    :param request: Словарь с email, lastName, firstName, middleName.
    :return: Ответ от сервера в виде объекта httpx.Response
    """

    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")

    """
    Метод удаления пользователя по идентификатору.
    :param user_id: Идентификатор пользователя.
    :return: Ответ от сервера в виде объекта httpx.Response
    """

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id=user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateUsersClient.
    """

    return PrivateUsersClient(client=get_private_http_client(user=user))
