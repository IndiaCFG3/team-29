from django.urls import path
from . import views
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login_view,name = 'login_view'),
    path('logout',views.logout_view,name = 'logout'),
    path('form1submit',views.form1submit,name = 'form1'),
    path('dashboard',views.dashboard,name = 'dashboard'),
]