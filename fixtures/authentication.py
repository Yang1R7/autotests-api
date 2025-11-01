import pytest
from pydantic import BaseModel, EmailStr
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()
