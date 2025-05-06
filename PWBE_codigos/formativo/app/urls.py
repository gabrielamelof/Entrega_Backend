from django.urls import path
from .views import LoginView, UsuarioListCreate, UsuarioRetrieveUpdateDestroy, ReservaAmbienteListCreate, ReservaAmbienteRetrieveUpdateDestroy, ReservaAmbienteProfessorList, DisciplinaListCreate, DisciplinaProfessorList, DisciplinaRetrieveUpdateDestroy,  SalaListCreate, SalaRetrieveUpdateDestroy

urlpatterns = [
    # Login
    path('login/', LoginView.as_view()), 

    # Usuário
    path('usuario/', UsuarioListCreate.as_view()),
    path('usuario/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view()),

    # Reserva Ambiente
    path('reservas/', ReservaAmbienteListCreate.as_view()), 
    path('reservas/<int:pk>/', ReservaAmbienteRetrieveUpdateDestroy.as_view()),
    path('professor/reservas/', ReservaAmbienteProfessorList.as_view()),

    #Disciplina
    path('disciplinas/', DisciplinaListCreate.as_view()), 
    path('disciplinas/<int:pk>/', DisciplinaRetrieveUpdateDestroy.as_view()),
    path('professor/disciplinas/', DisciplinaProfessorList.as_view()),

    # Sala
    path('sala/', SalaListCreate.as_view()),
    path('sala/<int:pk>/', SalaRetrieveUpdateDestroy.as_view()),



]

