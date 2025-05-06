from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer
from .permissions import IsGestor, IsProfessor, IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class UsuarioListCreate(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

class UsuarioRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'

class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return[IsAuthenticated()]
        return [IsGestor()]
    
class DisciplinaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'

class DisciplinaProfessorList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor=self.request.user)
    
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

# define as permissões. Caso seja GET, qualquer pessoa logada pode visualizar, caso o método seja outro, é necessário ser gestor para acessar
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()],
        return [IsGestor()]
    
    # Define a consulta pelo queryset, usando um filtro de id. caso contrário, retorna todos os dados cadastrados
    def get_queryset(self):
        queryset = super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            queryset = queryset.filter(professor_id=professor_id)
        return queryset 
    
class ReservaAmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsDonoOuGestor]
    lookup_field = 'pk'

class ReservaAmbienteProfessorList(ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor=self.request.user)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
