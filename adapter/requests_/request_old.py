import requests


class RequestOld:
    def __init__(self) -> None:
        pass

    @staticmethod
    def request() -> None:
        print(requests.get('https://www.google.com.br').text)


if __name__ == '__main__':
    request = RequestOld()
    request.request()
