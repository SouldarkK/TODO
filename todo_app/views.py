import datetime
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from todo_app.models import Todo
from todo_app.paginations import PageSize
from todo_app.serilazers import TodoListSerializer, TodoCreateSerializer
from rest_framework.permissions import AllowAny
from rest_framework import permissions


class TodoPagination(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Todo.active.all()
    serializer_class = TodoListSerializer
    pagination_class = PageSize




class TodoListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Todo.active.filter(created_by=request.user.id).all()
        serializer = TodoListSerializer(queryset, many=True)
        data = {
            "body": serializer.data,
            "totoal_size": queryset.count(),
            "status": status.HTTP_200_OK
        }
        return Response(data=data, status=status.HTTP_200_OK)




class TodoRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoListSerializer

    def get(self, request, pk: int = None, *args, **kwargs):
        model = Todo.object.get(pk=pk)
        ser = TodoListSerializer(model)
        data = {
            "body": ser.data,
            "status": status.HTTP_200_OK
        }
        return Response(data=data, status=status.HTTP_200_OK)




class TodoCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # http_method_names = ['POST']

    def post(self, request, *args, **kwargs):
        ser = TodoCreateSerializer(request.data)
        if ser.is_valid():
            instance = ser.save(created_by_id=request.user.id)
            data = {
                "body": ser.data,
                "created_at": datetime.datetime.now(),
                "id": instance.id,
                "status": status.HTTP_201_CREATED
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data={"Error": "Something wnt wrong"}, status=status.HTTP_409_CONFLICT)




class TodoDeleteAPIView(generics.DestroyAPIView):
    queryset = Todo.object.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        pk = int(kwargs['pk'])
        todo = self.queryset.filter(pk=pk)
        if todo.exists():
            todo.delete()
            data = {
                "Successfully deleted": "OK",
                "status": status.HTTP_404_NOT_FOUND
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)


        if todo.created_by_id.__ne__(request.user.id):
            data={
                "You are not allow to delete":request.user.id,
                "status":status.HTTP_403_FORBIDDEN
            }
            return Response(data=data , status=status.HTTP_403_FORBIDDEN)


class TodoComplateAPIView(APIView):
    queryset = Todo.active.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = int(kwargs['pk'])
        todo = self.queryset.filter(id=pk).first()

        if todo:
            return Response({"message": "The todo not found", "status": status.HTTP_404_NOT_FOUND})

        if todo.created_by_id.__ne__(request.data.id):
            return Response({"message": "You are not allowed", "status": status.HTTP_403_FORBIDDEN})

        todo.done = not todo.done
        todo.save()

