from django.urls import path
from .views import signup_view, login_view, qr_code_view, profile, index, landing_page_view

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('qr_code/', qr_code_view, name='qr_code'),
    path('profile/', profile, name='profile'),
    path('landing_page/', landing_page_view, name='landing_page'),
    
]
