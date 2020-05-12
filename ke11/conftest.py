import pytest

@pytest.fixture(scope="session")

def login_fixture1():
     print("前置操作：登录")