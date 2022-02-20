from rest_framework import status
from rest_framework.exceptions import APIException



class  FileNotFoundException(APIException):
    status_code=status.HTTP_404_NOT_FOUND
    default_code = {
        "message":"File not found",
        "status":status.HTTP_404_NOT_FOUND
    }
    default_detail = "Error"