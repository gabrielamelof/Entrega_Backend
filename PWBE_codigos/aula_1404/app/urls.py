from django.urls import path
from .views import PilotoListCreateAPIView, PilotoRetrieveUpdateDestroyAPIView, CarroListCreateAPIView, CarroRetrieveUpdateDestroyAPIView

# urls para definir as rotas de urls para cada view 
urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()), 
    path('piloto/<int:pk>', view=PilotoRetrieveUpdateDestroyAPIView.as_view()), 
    path('carro/', view=CarroListCreateAPIView.as_view()), 
    path('carro/<int:pk>', view=CarroRetrieveUpdateDestroyAPIView.as_view()), 
]