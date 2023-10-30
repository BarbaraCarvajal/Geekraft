from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . models import User
from . serializers import RegisterUserSerializer, MyTokenObtainPairSerializer

#Registro de usuarios
@api_view(['POST'])
def register(request):
  data = request.data
  user = User.objects.create(
    email=data['email'],
    name=data['name'],
    last_name=data['last_name'],
    password=make_password(data['password'])
  )
  serializer = RegisterUserSerializer(user, many=False) #many=False porque es un solo objeto
  return Response(serializer.data)

#Login con JWT
class LoginView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer