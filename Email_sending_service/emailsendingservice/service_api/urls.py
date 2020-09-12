from django.urls import path,include
from . import views

v1 = [
    path('email_info', views.email_info, name='email_info'),
    path('send_email', views.send_email, name='send_email')
]

urlpatterns = [
    path('v1/', include(v1))
]