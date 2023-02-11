from requests_ import RequestNew
from requests_ import RequestOld
from adapter import Adapter


class ClientRequest:
    @staticmethod
    def make_request():
        Adapter.make_request()


if __name__ == '__main__':
    #request = RequestOld()
    ClientRequest.make_request()
