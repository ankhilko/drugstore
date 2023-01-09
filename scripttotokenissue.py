from requests import Session



def post(url, json) -> dict:
    with Session() as session:
        response = session.post(
            url=url,
            json=json
        )
        with response.status_code == 200:
            return response.json()


if __name__ == '__main__':
    print(
        post(
            'http://localhost:8000/api/v1/login/',
            {"username": "admin", "password": "admin"},
        )
    )
