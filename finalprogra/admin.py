from django.contrib import admin
from finalprogra.models import Plato, PlatoAdmin, Menu, MenuAdmin
# Register your models here.
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Menu, MenuAdmin)
