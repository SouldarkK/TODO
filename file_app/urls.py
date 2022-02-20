from django.urls import path
from file_app.views import FileUploadView



urlpatterns=[
    path('upload/',FileUploadView.as_view(),name='upload'),
]