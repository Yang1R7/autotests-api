from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import GetUserResponseSchema
from pydantic_create_user import CreateUserRequestSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
from clients.users.private_users_client import get_private_users_client

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="test123",
    lastName="Max",
    firstName="Max",
    middleName="Max"
)
public_user_client = get_public_users_client()
create_user_response = public_user_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_user_client = get_private_users_client(user=authentication_user)

get_user_response = private_user_client.get_user_api(user_id=create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
