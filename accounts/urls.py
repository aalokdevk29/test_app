from django.urls import path
from .views import register_user, user_login, user_logout, verify_otp, update_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('update/<int:user_id>/', update_user, name='update_user'),
]