import  requests


host = "http://49.235.92.12:6009"

def get_token(username="test", psw="123456"):
    body = {
        "username": username,
        "password": psw
    }
    s = requests.session()
    r = s.post(host+"/api/vi/login", json=body)
    token = r.json()["token"]
    return token


if __name__ == '__main__':
    t = get_token()
    print(t)