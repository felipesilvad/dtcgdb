from django.contrib import admin
from .models import Card, Set, Digimon, New

admin.site.register(Card)

class SetAdmin(admin.ModelAdmin):
    pass

class DigimonAdmin(admin.ModelAdmin):
    pass

admin.site.register(New)

admin.site.register(Set, SetAdmin)

admin.site.register(Digimon, DigimonAdmin)


