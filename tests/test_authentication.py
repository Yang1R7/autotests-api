from http import HTTPStatus

import pytest

from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema, \
    CreateUserResponseSchema, PublicUsersClient
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from tests.conftest import UserFixture
from tools.assertions.assert_login_response import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login_api(request=request)
    response_data = LoginResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response=response_data)
    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
