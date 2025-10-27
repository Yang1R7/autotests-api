from clients.private_http_builder import AuthenticationUserDict
from clients.public_http_builder import get_public_http_client
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
  email = get_random_email(),
  password = "test123",
  lastName = "Max",
  firstName = "Max",
  middleName = "Max"
)

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(request=create_user_request)
print('Get create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email= create_user_request["email"],
    password= create_user_request["password"]
)
# Инициализируем клиент PrivateUsersClient
private_user_client = get_private_users_client(user=authentication_user)
# Отправляем GET запрос на получение данных пользователя
get_user_response = private_user_client.get_user(user_id=create_user_response["user"]["id"])
print('Get user data:', get_user_response)
