from django.contrib import admin
from .models import Usuario
from .models import Club
from .models import MiembroClub

admin.site.register(Usuario)
admin.site.register(Club)
admin.site.register(MiembroClub)
