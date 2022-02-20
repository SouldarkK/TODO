from rest_framework import status
from rest_framework.exceptions import APIException


class UsernameTaken(APIException):
    status_code = status.HTTP_200_OK
    default_detail = {
        "Username already taken":"Error"
    }
    default_code = 'Error'



class EmailTaken(APIException):
    status_code = status.HTTP_200_OK
    default_detail = {
        "Email already taken":"Error"
    }
    default_code = 'Error'



class PhoneTaken(APIException):
    status_code = status.HTTP_200_OK
    default_detail = {
        "Phone already taken":"Error"
    }
    default_code = 'Error'


class PasswordError(APIException):
    status_code = status.HTTP_200_OK
    default_detail = {
        "Passwords are not similar":"Error"
    }
    default_code = 'Error'


