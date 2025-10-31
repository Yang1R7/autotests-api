from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema, \
    CreateUserResponseSchema, PublicUsersClient
from http import HTTPStatus
import pytest
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request=request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_response(request=request, response=response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
