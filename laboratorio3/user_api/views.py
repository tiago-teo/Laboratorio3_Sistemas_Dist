from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from user_api.models import AppUser
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
from user_api.forms import RegisterForm, LoginForm
from django.shortcuts import redirect


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
		    return redirect('user')


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    
	##
    def get(self, request):
        serializer = UserSerializer(request.user)
        queryset = AppUser.objects.all()
        return Response({'user': queryset}, status=status.HTTP_200_OK)