import logging

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.template.defaulttags import csrf_token
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions

from TODO.erorrs import login_erorr
from auth_app.exceptions import UsernameTaken, EmailTaken, PhoneTaken, PasswordError
from auth_app.models import Employee
import jwt, datetime


class Logout(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    # http_method_names = ['GET']

    def post(self, request, *args, **kwargs):
        try:
            token = request.auth
            token = Token.objects.filter(key=token.key)
            if token.exists():
                token.delete()
                return Response(data={'Successfully deleted': "message", "status": status.HTTP_204_NO_CONTENT})
            return Response(data={'Something went wrong': 'error', "status": status.HTTP_409_CONFLICT},
                            status=status.HTTP_409_CONFLICT)
        except Exception as e:
            logging.error(e)
            return Response(data={"Something went wrong": "Error", "status": status.HTTP_409_CONFLICT},
                            status=status.HTTP_409_CONFLICT)


class Register(APIView):
    permission_classes = [permissions.AllowAny]

    # http_method_names = ['POST']

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            phone = request.data.get('phone')
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')
            picture_id = int(request.data.get('picture_id'))

            if User.objects.filter(username=username).exists():
                raise UsernameTaken()

            if User.objects.filter(email=email).exists():
                raise EmailTaken()

            if Employee.objects.filter(phone=phone).exists():
                raise PhoneTaken()

            if password.__ne__(confirm_password):
                raise PasswordError()

            User(username=username,
                 first_name=first_name,
                 last_name=last_name,
                 email=email,
                 password=make_password(password)).save()

            Employee(phone=phone, picture=picture_id, user=username).save()
            return Response(data={"User Registered": "OK", "status": status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error(e)
            return Response(data={"Something went wrong": "Error", "status": status.HTTP_409_CONFLICT},
                            status=status.HTTP_409_CONFLICT)


class Login(ObtainAuthToken):
    # permission_classes = [permissions.AllowAny]

    # http_method_names = ['POST']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.filter(user=user).first()
        if token:
            token.delete()
        token = Token(user=user)
        token.save()
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

    def permission_denied(self, request, message=None, code=None):
        message = "You are not allowed to enter to this site"
        code = status.HTTP_400_BAD_REQUEST
        return super().permission_denied(request, message, code, )

    def handle_exception(self, exc):
        return login_erorr(self, exc)

##################################################################################################################
#################################        JWT TOKEN                  ##############################################
##################################################################################################################

# class Login(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data['username']
#         password = request.data['password']
#
#         user = User.objects.filter(username=username).first()
#         if user is None:
#             raise AuthenticationFailed('Username Not Found ')
#
#         if not user.check_password(password):
#             raise AuthenticationFailed("Password Incorrect")
#
#         pyload = {
#             "id": user.id,
#             "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             "iat": datetime.datetime.utcnow()
#         }
#
#         token = jwt.encode(pyload, 'secret', algorithm="HS256")
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#
#         return Response(data={'jwt': token}, status=status.HTTP_200_OK)


# class Auth(APIView):
#     """
#     For Authenticate the user
#     """
#
#     def get(self, request, *args, **kwargs):
#         token = request.COOKIES.get('jwt')
#         if token is None:
#             raise AuthenticationFailed("User did not Authenticate")
#
#         try:
#             payload = jwt.encode(token, 'secret', algorithm=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed("User did not Authenticate")
#
#
#         user=User.objects.get(payload['id'])
#
#         return Response(data={"user":user}, status=status.HTTP_200_OK)




#
# class Logout(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     # http_method_names = ['GET']
#
#     def post(self, request, *args, **kwargs):
#         response = Response()
#         response.delete_cookie("jwt")
#         response.data = {
#             "successfully deleted": "DELETE",
#             "status": status.HTTP_404_NOT_FOUND
#         }
#         return Response(data=response, status=status.HTTP_404_NOT_FOUND)

