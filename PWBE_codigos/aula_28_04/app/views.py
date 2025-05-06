from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer, IngressoSerializer, LoginSerializer
from .permissions import IsGestor, IsGestorOuDono
from .models import Usuario, Ingresso
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]


class IngressoRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.objects
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestorOuDono]

class IngressoListCreateAPIView(ListCreateAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

