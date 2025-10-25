import httpx

from tools.fakers import get_random_email

payload = {
  "email": get_random_email(),
  "password": "test123",
  "lastName": "Max",
  "firstName": "Max",
  "middleName": "Max"
}


response = httpx.post('http://localhost:8000/api/v1/users', json=payload)
print(response.json())
print(response.status_code)
