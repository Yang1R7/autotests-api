import httpx



login_paylod = {
    "email": "maxim@gmail.com",
    "password": "futbol"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_paylod)
assert login_response.status_code == 200, f"Ожидался код ответа 200, получен: {login_response.status_code}"

login_data = login_response.json()
access_token_value = login_data.get("token").get("accessToken")
auth_headers = {"Authorization": f"Bearer {access_token_value}" }

get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=auth_headers)
assert get_user_response.status_code == 200, f"Ожидался код ответа 200, получен: {get_user_response.status_code}"
print(get_user_response.json())





