from django.contrib import admin

from empresa.models import TipoVinculacion, TipoNivelRiesgo, NivelRiesgo, Empresa, Cargo, Vinculacion

# Register your models here.

admin.site.register(TipoVinculacion)
admin.site.register(TipoNivelRiesgo)
admin.site.register(NivelRiesgo)
admin.site.register(Empresa)
admin.site.register(Cargo)
admin.site.register(Vinculacion)
