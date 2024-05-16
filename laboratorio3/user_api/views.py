from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from user_api.models import AppUser
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, PackSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
from user_api.forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from .models import Package
from itertools import chain

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_register.html'
    def get(self,request):
        context = RegisterForm()
        return Response({'form': context}, status=status.HTTP_200_OK)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return redirect('login')
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    ##
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_login.html'
    def get(self,request):
        context = LoginForm()
        return Response({'form': context}, status=status.HTTP_200_OK)
    def post(self, request):
	    data = request.data
	    assert validate_email(data)
	    assert validate_password(data)
	    serializer = UserLoginSerializer(data=data)
	    if serializer.is_valid(raise_exception=True):
		    user = serializer.check_user(data)
		    login(request, user)
		    return redirect('package')


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def get(self, request):
		logout(request)
		return redirect('/')



class Packages(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'package_list.html'
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = PackSerializer
        username = request.user.username
        if request.GET.get('search'):
            pack = Package.objects.filter(pack_id=request.GET.get('search'), sender=username) | Package.objects.filter(pack_id=request.GET.get('search'), receiver=username) | Package.objects.filter(pack_id=request.GET.get('search'), name=username)
        else:
            pack = Package.objects.filter(sender=username) | Package.objects.filter(receiver=username) | Package.objects.filter(name=username)
        return Response({'pack': pack}, status=status.HTTP_200_OK)


class Dashboard(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'

    def get(self, request):
        return Response(status=status.HTTP_200_OK)