import httpx


login_payload = {
    "email": "maxim@gmail.com",
    "password": "futbol"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"],
}

print("Login Response:",login_response_data)
print("Status code:", login_response.status_code)

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh Response:",refresh_response_data)
print("Status code:", refresh_response.status_code)
