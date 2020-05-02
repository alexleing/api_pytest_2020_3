import pytest
import requests
from .comm import com_f

key = '61453cf60a746632636b89647c779d32'
key1 = ''
key2 ='123'

@pytest.fixture()
def key_get():
    s = com_f(key)
    return s


@pytest.fixture()
def wrong_key():
    s = com_f(key2)
    return s


@pytest.fixture()
def null_key():
    s = com_f(key1)
    return s
# if __name__ == '__main_':
#     key1 = '123'
#     a = null_key(key1)
#     print(a)

