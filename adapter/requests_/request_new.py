import httpx


class RequestNew:
    def __init__(self) -> None:
        pass

    @staticmethod
    def request() -> None:
        print(httpx.get('https://www.google.com.br').text)


if __name__ == '__main__':
    request = RequestNew()
    request.request()
