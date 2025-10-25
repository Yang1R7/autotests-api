import httpx


response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = {
    "userId": 11,
    "title": "Новая задача",
    "completed": True,
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos",json=data)

print(response.status_code)
print(response.json())


data = {"username": "Maxim", "password": "12345"}

response = httpx.post("https://httpbin.org/post", data = data)

print(response.status_code)
print(response.json())


headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers = headers)

print(response.request.headers)
print(response.json())

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.json())


file = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=file)
print(response.json())

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")

print(response.json())
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    print(response.status_code)
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысел лимит времени")
