from django.contrib import admin

from receita.models import Receita

class ListandoReceita(admin.ModelAdmin):
    list_display = ("id", "descricao", "valor", "descricao", "paga", "data")
    list_display_links = ("id","descricao")
    search_fields = ("descricao",)
    list_filter = ("descricao","valor", "data")
    list_editable = ("paga",)
    list_per_page = 10

admin.site.register(Receita, ListandoReceita)