# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
#
# # Create your views here.
#
# def indexView(request):
#     return render(request, 'index.html')
#
# @login_required
# def dashboardView(request):
#     return render(request, 'dashboard.html')
#
#
# def registerView(request):
#     if request.method == "POST":
#         print(request)
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_url')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'registration/register.html', {'form': form })

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from accounts.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/accounts/token/',
        '/accounts/register/',
    ]
    return Response(routes)