from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import  MultiPartParser

from file_app.exception import FileNotFoundException
from file_app.models import File
from file_app.utels import upload_file
from rest_framework import permissions

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if "file" not in request.data:
            raise FileNotFoundException()
        file: File = upload_file(request.data['file'])
        response = {
            "message": {
                "file_id": file.id,
                "name": file.name,
                "content_type": file.content_type,
                "gen_name": file.gen_name,
                "size": file.size,
                'request_taken_tiem': 1
            },
            "status": status.HTTP_200_OK
        }
        return Response(response)

    def handle_exception(self, exc):
        return super().handle_exception(exc)

