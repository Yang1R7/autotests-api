import pytest

from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_number_1(number):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host",
                         ["https://dev.company.com", "https://stage.company.com", "https://prod.company.com"])
def test_multiplication_of_numbers(os, host):
    assert len(os + host) > 0


@pytest.fixture(params=["https://dev.company.com",
                        "https://stage.company.com",
                        "https://prod.company.com"])
def host(request: SubRequest):
    return request.param


def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    def test_user_with_operations(self, user):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user):
        print(f"User without operations: {user}")


user = {"11": "User 1",
        "22": "User 1",
        "33": "User 1"}


@pytest.mark.parametrize("phone_number", user.keys(),
                         ids=lambda phone_number: f"{phone_number}: {user[phone_number]}")
def test_identifiers(phone_number: str):
    pass
