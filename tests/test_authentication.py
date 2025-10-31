from http import HTTPStatus

import pytest

from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema, CreateUserResponseSchema
from clients.authentication.authentication_client import get_authentication_client
from tools.assertions.assert_login_response import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_client = get_public_users_client()
    request = CreateUserRequestSchema()
    create_user = public_client.create_user_api(request)

    authentication_client = get_authentication_client()

    login_data = LoginRequestSchema(email=request.email, password=request.password)
    login_response = authentication_client.login_api(request=login_data)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(response=login_response_data)
    validate_json_schema(instance=login_response.json(), schema=login_response_data.model_json_schema())
