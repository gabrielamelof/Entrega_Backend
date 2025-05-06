from django.contrib import admin
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields" : (
                'tipo', 'ni', 'telefone'
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields" : (
                'tipo', 'ni', 'telefone', 'data_nascimento', 'data_contratacao'
            ),
        }),
    )

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Disciplina)
admin.site.register(ReservaAmbiente)
admin.site.register(Sala)