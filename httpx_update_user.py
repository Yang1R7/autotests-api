import httpx

from tools.fakers import get_random_email

create_user_payload = {
  "email": get_random_email(),
  "password": "test123",
  "lastName": "Max",
  "firstName": "Max",
  "middleName": "Max"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users",json=create_user_payload)
assert create_user_response.status_code == 200, f"Ожидался код ответа 200, получен: {create_user_response.status_code}"

create_user_data = create_user_response.json()
login_payload = {
    "email": create_user_payload.get("email"),
    "password": create_user_payload.get("password")
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
assert login_response.status_code == 200, f"Ожидался код ответа 200, получен: {login_response.status_code}"
login_response_data = login_response.json()


update_headers_token = {"Authorization": f"Bearer {login_response_data.get("token").get("accessToken")}"}
update_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_data.get("user").get("id")}",
                                    headers=update_headers_token, json=update_payload)
assert  update_user_response.status_code == 200, f"Ожидался код ответа 200, получен: {update_user_response.status_code}"

update_data_response = update_user_response.json()
print(update_data_response)
print("Старый email:", create_user_payload.get("email"))
print("Новый email:", update_data_response.get("user").get("email"))
