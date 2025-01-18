# import requests
#
# BASE_URL = "http://127.0.0.1:8000"
#
#
# def register_user(username, password):
#     url = f"{BASE_URL}/api/register"
#     data = {"username": username, "password": password}
#     response = requests.post(url, json=data)
#     print(f"Register Response: {response.status_code}, {response.json()}")
# def login(username, password):
#     url = f"{BASE_URL}/api/login"
#     data = {"username": username, "password": password}
#     response = requests.post(url, json=data)
#     print(f"Login Response: {response.status_code}, {response.json()}")
# def baza():
#     url = f"{BASE_URL}/users"
#     response = requests.get(url)
#     print(f"Baza dannych: {response.status_code}, {response.json()}")
#
# if __name__ == "__main__":
#     print("Registering user...")
#     register_user("test", "test")
#
#     print("Registering user...")
#     register_user("test", "test")
#
#     print("Logging user...")
#     login("test", "test")
#
#     print("Getting user...")
#     baza()