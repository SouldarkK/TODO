from django.urls import path

from todo_app.views import TodoPagination, TodoListView, TodoRetrieveView, TodoCreateView, TodoDeleteAPIView, \
    TodoComplateAPIView

urlpatterns=[
    path('page/',TodoPagination.as_view(),name='pagination'),
    path('todo_list/',TodoListView.as_view(),name='pagination'),
    path('todo_one/<int:pk>',TodoRetrieveView.as_view(),name='pagination'),
    path('todo_create/',TodoCreateView.as_view(),name='pagination'),
    path('todo_delete/<int:pk>',TodoDeleteAPIView.as_view(),name='pagination'),
    path('todo_finish/<int:pk>',TodoComplateAPIView.as_view(),name='pagination'),
]