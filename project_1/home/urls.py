
from django.urls import path
from .views import signup_view, login_view, qr_code_view,profile

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('qr_code/', qr_code_view, name='qr_code'),
    path('profile/', profile, name='profile'),
    # Add more URL patterns as needed
]

