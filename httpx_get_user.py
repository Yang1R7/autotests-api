import httpx

from tools.fakers import fake

create_user_payload = {
  "email": fake.email(),

  "password": "test123",
  "lastName": "Max",
  "firstName": "Max",
  "middleName": "Max"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users",json=create_user_payload)

create_user_data = create_user_response.json()
login_payload = {
    "email": create_user_payload.get("email"),
    "password": create_user_payload.get("password")
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()

headers_token = {"Authorization": f"Bearer {login_response_data.get("token").get("accessToken")}"}

get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_data.get("user").get("id")}",
                              headers=headers_token)
get_user_response_data = get_user_response
print(get_user_response_data)