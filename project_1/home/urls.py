from django.urls import path
from .views import index, signup_view, login_view, landing, logout_view, qr_code_view, profile

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('landing/', landing, name='landing'),
    path('logout/', logout_view, name='logout'),
    path('qr_code/', qr_code_view, name='qr_code'),
   
]