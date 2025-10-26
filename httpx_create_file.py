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

create_user_data = create_user_response.json()
login_payload = {
    "email": create_user_payload.get("email"),
    "password": create_user_payload.get("password")
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()

create_file_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    headers=create_file_headers,
    data={"filename": "image.png",
          "directory": "courses"},
    files={"upload_file":open("./testdata/files/image.png", "rb")}
)

create_file_response_data = create_file_response.json()
print(create_file_response_data)