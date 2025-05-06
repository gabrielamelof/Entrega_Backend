from django.shortcuts import render
from .models import Postagem

# Create your views here.
def listar_postagens(request):
    postagens = Postagem.objects.all().order_by('-data_criacao')
    return render(request, 'blog/luana.html', {'postagens':postagens})
