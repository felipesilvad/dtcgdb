from django.contrib import admin
from .models import Card, Set, Digimon, New, AlternateArt, Effect, EffectKeyword

admin.site.register(Card)

admin.site.register(AlternateArt)

admin.site.register(Effect)

admin.site.register(EffectKeyword)

class SetAdmin(admin.ModelAdmin):
    pass

class DigimonAdmin(admin.ModelAdmin):
    pass

admin.site.register(New)

admin.site.register(Set, SetAdmin)

admin.site.register(Digimon, DigimonAdmin)


