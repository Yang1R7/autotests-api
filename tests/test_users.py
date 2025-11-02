from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema, \
    CreateUserResponseSchema, PublicUsersClient
from http import HTTPStatus
import pytest

from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize("email", ["mail.ru", "gmail.com","example.com"])
def test_create_user(email, public_users_client: PublicUsersClient):
    request = CreateUserRequestSchema(email=fake.email(domain=email))
    response = public_users_client.create_user_api(request=request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_response(request=request, response=response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user, private_users_client):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_get_user_response(get_user_response=response_data,
                             create_user_response=function_user.response)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
