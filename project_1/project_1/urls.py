# urls.py
from django.urls import path

from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('landing/', views.landing_view, name='landing'),
    path('qr_code/<int:receipt_id>/', views.qr_code_view, name='qr_code'),
]
