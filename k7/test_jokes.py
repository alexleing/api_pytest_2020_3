import requests
import allure


@allure.story("test_joke_1")
def test_joke_1(key_get):
    key = key_get
    print(key)
    assert key.json()['reason'] == 'Success'


@allure.story("test_joke_2")
def test_joke_2(wrong_key):
    key = wrong_key
    print(key)
    assert key.json()['resultcode'] == '101'


@allure.story("test_joke_3")
def test_joke_3(null_key):
    key = null_key
    print(key)
    assert key.json()['resultcode'] == '101'





