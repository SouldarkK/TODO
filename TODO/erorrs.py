from rest_framework import status
from rest_framework.response import Response


def login_erorr(self, exc):
    if exc == status.HTTP_400_BAD_REQUEST:
        return Response(data={'Bad request': 'error', 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
    elif exc == status.HTTP_401_UNAUTHORIZED:
        return Response(data={'UNAUTHORIZED': 'error', 'status': status.HTTP_401_UNAUTHORIZED},
                        status=status.HTTP_401_UNAUTHORIZED)

    elif exc == status.HTTP_402_PAYMENT_REQUIRED:
        return Response(data={'PAYMENT_REQUIRED': 'error', 'status': status.HTTP_402_PAYMENT_REQUIRED},
                        status=status.HTTP_402_PAYMENT_REQUIRED)


    elif exc == status.HTTP_403_FORBIDDEN:
        return Response(data={'FORBIDDEN': 'error', 'status': status.HTTP_403_FORBIDDEN},
                        status=status.HTTP_403_FORBIDDEN)

    elif exc == status.HTTP_404_NOT_FOUND:
        return Response(data={'NOT_FOUND': 'error', 'status': status.HTTP_404_NOT_FOUND},
                        status=status.HTTP_404_NOT_FOUND)


    elif exc == status.HTTP_405_METHOD_NOT_ALLOWED:
        return Response(data={'METHOD_NOT_ALLOWED': 'error', 'status': status.HTTP_405_METHOD_NOT_ALLOWED},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)


    elif exc == status.HTTP_406_NOT_ACCEPTABLE:
        return Response(data={'NOT_ACCEPTABLE': 'error', 'status': status.HTTP_406_NOT_ACCEPTABLE},
                        status=status.HTTP_406_NOT_ACCEPTABLE)

    elif exc == status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED:
        return Response(data={'PROXY_AUTHENTICATION_REQUIRED': 'error',
                              'status': status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED},
                        status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

    elif exc == status.HTTP_408_REQUEST_TIMEOUT:
        return Response(data={'REQUEST_TIMEOUT': 'error', 'status': status.HTTP_408_REQUEST_TIMEOUT},
                        status=status.HTTP_408_REQUEST_TIMEOUT)


    elif exc == status.HTTP_409_CONFLICT:
        return Response(data={'CONFLICT': 'error', 'status': status.HTTP_409_CONFLICT},
                        status=status.HTTP_409_CONFLICT)

    else:
        return Response(data={'Something went wrong': "ERROR", 'status': status.HTTP_409_CONFLICT},
                        status=status.HTTP_409_CONFLICT)
