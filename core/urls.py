from django.conf.urls import url
from . import auth_views, views

urlpatterns = [
    url(r'login/$', auth_views.login, name='login'),
    url(r'register/$', auth_views.register, name='register'),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'order/$', views.order, name='order'),
]
