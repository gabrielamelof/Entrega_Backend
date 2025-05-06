from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Piloto, Carro
from .serializers import PilotoSerializer, CarroSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
# Classe pra definir o tamanho da página e fazer a paginação
class PilotoPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


#View para criar e listar os pilotos cadastrados no banco de dados 
class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

# Para a documentação da APi com o swagger
    @swagger_auto_schema(
            operation_description='Lista todos os pilotos de fórmula 1', 
            responses={
                200: PilotoSerializer(many=True), 
                400: 'Error', 
            }, 
            manual_parameters=[
                openapi.Parameter(
                    'nome', 
                    openapi.IN_QUERY, 
                    description='Filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )
            ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_description='Cria um novo piloto', 
            request_body = PilotoSerializer, 
            responses={
                201: PilotoSerializer,
                400: 'ERROOOOOO'
            }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a DS16 deve ficar entre os 5 primeiros')
        serializer.save()

# View para atualizar ou deletar um piloto cadastrado no banco de dados pelo seu id   
class PilotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk'

# Adiciona uma descrição e status http para o get da view PilotoRetrieveUpdateDestroyAPIView na documentação da API
    @swagger_auto_schema(
        operation_description='Pega o piloto do ID fornecido', 
        responses={
            200: PilotoSerializer, 
            404: 'Not Found', 
            400: 'Error'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
            operation_description='Atualiza os dados de um piloto especifico a partir de seu ID', 
            request_body = PilotoSerializer, 
            responses={
                201: PilotoSerializer,
                400: 'ERROOOOOO'
            }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_description='Atualiza parcialmente od dados de um piloto especicifo com base em seu id que é passado como parâmetro', 
            request_body = PilotoSerializer, 
            responses={
                201: PilotoSerializer,
                400: 'ERROOOOOO'
            }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description='deleta os dados do piloto correspondente com o ID passado', 
        responses={
            200: PilotoSerializer, 
            404: 'Not Found', 
            400: 'Error'
        }
    )
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    
# Views para o carro

# Classe pra definir o tamanho da página e fazer a paginação
class CarroPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

#View para criar e listar os carros cadastrados no banco de dados 
class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPaginacao

# Para a documentação dos carros com o Swagger
    @swagger_auto_schema(
            operation_description='Lista todos os carros armazenados no banco de dados', 
            responses={
                200: CarroSerializer(many=True), 
                400: 'Error', 
            }, 
            manual_parameters=[
                openapi.Parameter(
                    'nome', 
                    openapi.IN_QUERY, 
                    description='Filtra pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )
            ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_description='Para criar um novo elemento carro', 
            request_body = CarroSerializer, 
            responses={
                201: CarroSerializer,
                400: 'ERROOOOOO'
            }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    

# View para atualizar ou deletar um carro cadastrado no banco de dados pelo seu id   
class CarroRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field = 'pk'

# Adiciona uma descrição e status http para o get da view PilotoRetrieveUpdateDestroyAPIView na documentação da API
    @swagger_auto_schema(
        operation_description='Pega o carro do ID fornecido pelo usuário', 
        responses={
            200: CarroSerializer, 
            404: 'Not Found', 
            400: 'Error'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
            operation_description='Atualiza os dados de um piloto especifico a partir de seu ID', 
            request_body = CarroSerializer, 
            responses={
                201: CarroSerializer,
                400: 'ERROOOOOO'
            }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_description='Atualiza parcialmente os dados de um carro especifico com base em seu id que é passado como parâmetro', 
            request_body = CarroSerializer, 
            responses={
                201: CarroSerializer,
                400: 'ERROOOOOO'
            }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description='deleta os dados do carro correspondente com o ID passado', 
        responses={
            200: CarroSerializer, 
            404: 'Not Found', 
            400: 'Error'
        }
    )
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    