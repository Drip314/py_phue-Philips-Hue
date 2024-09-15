from scripts import philip
from django.shortcuts import render


def myview(request):
    if request.POST.get('main') == "toggle":
        philip.on_off(request.POST.getlist('lamp'))

    context = {
        'lights': philip.get_lights()
    }

    return render(request, 'index.html', context=context)
