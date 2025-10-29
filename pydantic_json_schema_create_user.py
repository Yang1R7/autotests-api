import jsonschema
from jsonschema import validate

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="test123",
    lastName="Max",
    firstName="Max",
    middleName="Max"
)

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user_api(request=create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()


validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

print(create_user_response_schema)
print(create_user_response.json())
