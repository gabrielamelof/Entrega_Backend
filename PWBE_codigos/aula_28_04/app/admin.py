from django.contrib import admin
from .models import Ingresso, Usuario, Empresa
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields" : (
                'apelido', 'telefone', 'genero', 'colaborador', 'empresa'
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields" : (
                'apelido', 'telefone', 'genero', 'colaborador', 'empresa'
            ),
        }),
    )
    
admin.site.register(Ingresso)
admin.site.register(Empresa)
admin.site.register(Usuario, UsuarioAdmin)



