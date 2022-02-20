from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth_app.views import Login, Logout, Register

urlpatterns=[
    path('login/',Login.as_view(),name='login'),
    path('logout/<int:pk>/',Logout.as_view(),name='logout'),
    path('register/',Register.as_view(),name='register'),
    # path('user/',Auth.as_view(),name='user'),

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/', MyTokenObtainPairSerializer, name='token_obtain_pair'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]