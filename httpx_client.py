import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()
client = httpx.Client(base_url="http://localhost:8000", timeout=100
                      ,headers={"Authorization": f"Bearer {login_response_data.get("token").get("accessToken")}"})

get_user_me = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me.json()

print("Get user me data:", get_user_me_response_data)