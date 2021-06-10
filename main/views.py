from typing import ChainMap
from django.shortcuts import render 
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


def index(request):
    complete_pc = Complete_PC.objects.order_by('-price')
    return render(request, 'main/index.html', {
        'complete_pc': complete_pc
    })

    
def complete(request):
    complete_pc = Complete_PC.objects.order_by('-price')
    return render(request, 'main/complete.html', {
        'complete_pc': complete_pc
    }) 


def catalog_max(request):
    cpu_max = CPU.objects.order_by('-price')
    cpu_min = CPU.objects.order_by('price')

    case_max = Case.objects.order_by('-price')
    case_min = Case.objects.order_by('price')

    mainboard_max = Mainboard.objects.order_by('-price')
    mainboard_min = Mainboard.objects.order_by('price')

    videocard_max = VideoCard.objects.order_by('-price')
    videocard_min = VideoCard.objects.order_by('price')

    ram_max = RAM.objects.order_by('-price')
    ram_min = RAM.objects.order_by('price')

    ssd_max = SSD.objects.order_by('-price')
    ssd_min = SSD.objects.order_by('price')

    hdd_max = HDD.objects.order_by('-price')
    hdd_min = HDD.objects.order_by('price')

    cooler_max = Cooler.objects.order_by('-price')
    cooler_min = Cooler.objects.order_by('price')

    powerSupplyUnit_max = PowerSupplyUnit.objects.order_by('-price')
    powerSupplyUnit_min = PowerSupplyUnit.objects.order_by('price')
    

    return render(request, 'main/catalog_max.html', {
        'cpu_max': cpu_max,
        'cpu_min': cpu_min,

        'case_min': case_min,
        'case_max': case_max,

        'mainboard_max': mainboard_max,
        'mainboard_min': mainboard_min,

        'videocard_max': videocard_max,
        'videocard_min': videocard_min,

        'ram_max': ram_max,
        'ram_min': ram_min,

        'ssd_max': ssd_max,
        'ssd_min': ssd_min,

        'hdd_max': hdd_max,
        'hdd_min': hdd_min,

        'cooler_max': cooler_max,
        'cooler_min': cooler_min,

        'powerSupplyUnit_max': powerSupplyUnit_max,
        'powerSupplyUnit_min': powerSupplyUnit_min
    })


def catalog(request):
    cpu_max = CPU.objects.order_by('-price')
    cpu_min = CPU.objects.order_by('price')

    case_max = Case.objects.order_by('-price')
    case_min = Case.objects.order_by('price')

    mainboard_max = Mainboard.objects.order_by('-price')
    mainboard_min = Mainboard.objects.order_by('price')

    videocard_max = VideoCard.objects.order_by('-price')
    videocard_min = VideoCard.objects.order_by('price')

    ram_max = RAM.objects.order_by('-price')
    ram_min = RAM.objects.order_by('price')

    ssd_max = SSD.objects.order_by('-price')
    ssd_min = SSD.objects.order_by('price')

    hdd_max = HDD.objects.order_by('-price')
    hdd_min = HDD.objects.order_by('price')

    cooler_max = Cooler.objects.order_by('-price')
    cooler_min = Cooler.objects.order_by('price')

    powerSupplyUnit_max = PowerSupplyUnit.objects.order_by('-price')
    powerSupplyUnit_min = PowerSupplyUnit.objects.order_by('price')
    

    return render(request, 'main/catalog.html', {
        'cpu_max': cpu_max,
        'cpu_min': cpu_min,

        'case_min': case_min,
        'case_max': case_max,

        'mainboard_max': mainboard_max,
        'mainboard_min': mainboard_min,

        'videocard_max': videocard_max,
        'videocard_min': videocard_min,

        'ram_max': ram_max,
        'ram_min': ram_min,

        'ssd_max': ssd_max,
        'ssd_min': ssd_min,

        'hdd_max': hdd_max,
        'hdd_min': hdd_min,

        'cooler_max': cooler_max,
        'cooler_min': cooler_min,

        'powerSupplyUnit_max': powerSupplyUnit_max,
        'powerSupplyUnit_min': powerSupplyUnit_min
    })
