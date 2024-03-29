import threading
import time
import uuid

from rest_framework.request import Request

from file_app.exception import FileNotFoundException
from file_app.models import File
from TODO.settings import FILE_UPLOAD_DIR

from os.path import join as join_path


def get_extension(filename: str) -> str:
    return filename.split(".")[-1]


def unique_code() -> str:
    return "%s%s" % (time.time_ns(), str(uuid.uuid4()).replace("-", ""))


def upload_path() -> str:
    return FILE_UPLOAD_DIR


def gen_new_name(file) -> str:
    return "%s.%s" % (unique_code(), get_extension(filename=file.name))


def upload_file(file):
    name = file.name
    size = file.size
    gen_name = gen_new_name(file)
    content_type = file.content_type
    extension = get_extension(filename=file.name)
    uploaded_file = File(name=name,
                         size=size,
                         gen_name=gen_name,
                         content_type=content_type,
                         extension=extension)
    uploaded_file.save()

    path = join_path(upload_path(), gen_name)

    for chunk in file.chunks():
        with open(path, "wb+") as wr:
            wr.write(chunk)

    return uploaded_file


