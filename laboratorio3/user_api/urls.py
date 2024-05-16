from django.urls import path
from . import views

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('package', views.Packages.as_view(), name='package'),
	path('', views.Dashboard.as_view(), name='dashboard'),
]