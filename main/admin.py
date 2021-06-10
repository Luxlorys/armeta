from django.contrib import admin
from .models import (
    Case,
    CPU,
    Mainboard, 
    VideoCard,
    RAM, 
    SSD,
    HDD,
    Cooler,
    PowerSupplyUnit,
    Complete_PC
    )


class CaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Case, CaseAdmin)
admin.site.register(CPU)
admin.site.register(Mainboard)
admin.site.register(VideoCard)
admin.site.register(RAM)
admin.site.register(SSD)
admin.site.register(HDD)
admin.site.register(Cooler)
admin.site.register(PowerSupplyUnit)
admin.site.register(Complete_PC)