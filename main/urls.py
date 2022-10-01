from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('registration', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_user, name='profile')
]
